import streamlit as st

#st.markdown('<style>body{background-color: #D2E9FF;}</style>',unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://github.com/NTUT530/Streamlit_learning/blob/main/mix_design/image.PNG?raw=true")
    }
   .sidebar .sidebar-content {
        background: url("https://github.com/NTUT530/Streamlit_learning/blob/main/mix_design/image.PNG?raw=true")
    }
    </style>
    """,
    unsafe_allow_html=True
)

#st.header('IS 10262 混凝土混合設計 - 混凝土混合比例')
st.write('<font size="7"><center><b>IS 10262 混凝土混合設計<br>混凝土混合比例</b></center></font>',unsafe_allow_html=True)


##
li1=st.write('<font size="4">等級</font>',unsafe_allow_html=True)
col1,col2 = st.beta_columns(2)
with col1:
    Grade_designation = st.selectbox(li1,['M10','M15','M20','M25','M30','M35','M40'])

#CA = Coarse Aggregate (粗骨料)
#W_C= Water content (含水量)
#charact_str = widgets.Dropdown(value = 20,options=[10,15,20,25,30,35,40],description='fck')
#standard_dev = widgets.FloatSlider(value = 4,options=[3.5,4,5],description='Standard Deviation',style=style)
#Max_Nominal_size_CA = st.slider('Nominal Max size of Coarse Aggregate',min_value=10,max_value=40,value=20)
with col2:
    Max_Nominal_size_CA = st.text_input(label='粗骨料的標稱最大尺寸(mm)',value='20')

Exposure_Condition = st.selectbox('軟硬程度',['軟','中等','硬','非常硬','極限'])

#Minimum_Cement_Content = st.selectbox('最小水泥含量:kg/m3',[340,360,380,400,300,320,360,270,290,310,330])

#Max_WC_Ratio = st.text_area(label='Max WC Ratio',value='0.5')   ## Maximum water cement ratio from table
##From IS456:2000
def max_CA_change(Max_Nominal_size_CA,Exposure_Condition):
    ## to change value on max CA size
    if Max_Nominal_size_CA == '20':
            ## to change value based on exposure condition
            if Exposure_Condition == '軟':
                Minimum_Cement_Content = 300
                Max_WC_Ratio = 0.55
                Max_Wcontet_CAgg = 186
            elif Exposure_Condition == '中等':
                Minimum_Cement_Content = 300
                Max_WC_Ratio = 0.5
                Max_Wcontet_CAgg = 186
            elif Exposure_Condition == '硬':
                Minimum_Cement_Content = 320
                Max_WC_Ratio = 0.45
                Max_Wcontet_CAgg = 186
            elif Exposure_Condition == '非常硬':
                Minimum_Cement_Content = 340
                Max_WC_Ratio = 0.45
                Max_Wcontet_CAgg = 186
            else:
                Minimum_Cement_Content.value = 360
                Max_WC_Ratio.value = 0.40
                Max_Wcontet_CAgg.value = 186


    elif Max_Nominal_size_CA == '10':

            if Exposure_Condition == '軟':
                Minimum_Cement_Content = 340
                Max_WC_Ratio = 0.55
                Max_Wcontet_CAgg = 208
            elif Exposure_Condition == '中等':
                Minimum_Cement_Content = 340
                Max_WC_Ratio = 0.50
                Max_Wcontet_CAgg = 208
            elif Exposure_Condition == '硬':
                Minimum_Cement_Content = 360
                Max_WC_Ratio = 0.45
                Max_Wcontet_CAgg = 208
            elif Exposure_Condition == '非常硬':
                Minimum_Cement_Content = 380
                Max_WC_Ratio = 0.45
                Max_Wcontet_CAgg = 208
            else:
                Minimum_Cement_Content = 400
                Max_WC_Ratio = 0.40
                Max_Wcontet_CAgg = 208
    else:
            ## Max CA size = 40 mm
            if Exposure_Condition == '軟':
                Minimum_Cement_Content = 270
                Max_WC_Ratio = 0.55
                Max_Wcontet_CAgg = 165
            elif Exposure_Condition == '中等':
                Minimum_Cement_Content = 270
                Max_WC_Ratio = 0.50
                Max_Wcontet_CAgg = 165
            elif Exposure_Condition == '硬':
                Minimum_Cement_Content = 290
                Max_WC_Ratio = 0.45
                Max_Wcontet_CAgg = 165
            elif Exposure_Condition == '非常硬':
                Minimum_Cement_Content = 310
                Max_WC_Ratio = 0.45
                Max_Wcontet_CAgg = 165
            else:
                Minimum_Cement_Content = 330
                Max_WC_Ratio = 0.40
                Max_Wcontet_CAgg = 165

    return Minimum_Cement_Content,Max_WC_Ratio,Max_Wcontet_CAgg


col3,col4,col5 = st.beta_columns(3)
with col3:
    c=max_CA_change(Max_Nominal_size_CA,Exposure_Condition)
    Minimum_Cement_Content = c[0]
    d=str(c[0])
    dd=st.text_input(label='最低水泥含量',value=d)

with col4:
    Max_WC_Ratio = c[1]
    f=str(c[1])
    ff=st.text_input(label='最大水泥比例',value=f)

with col5:
    Max_Wcontet_CAgg=c[2]
    g=str(c[2])
    gg=st.text_input(label='最大水泥比重',value=g)

col6,col7 = st.beta_columns(2)
with col6:
    Prac_WC_Ratio = st.slider(label='輸入砂漿比例',value=0.5,min_value=0.4,max_value=0.8)
with col7:
    Workability = st.slider(value=50.00,min_value=10.00,max_value=500.00,step=5.00,label='坍度(mm)')

col8,col9 = st.beta_columns(2)
with col8:
    Method_placing = st.radio('放置方法 :',['手動','電動'])
with col9:
    reduction = st.slider(value=15,min_value=1,max_value=20,step=1,label='減少混泥土配比')


Mass_Admixture_perc = st.slider(value=1.2,min_value=1.0,max_value=40.0,step=0.1,label='水泥潤滑劑(kg)')

col12,col13 = st.beta_columns(2)
with col12:
    Zone = st.selectbox('限制點火源能量',['隔爆型','增安型','正壓型','粉塵防爆型'])
 
##From IS456:2000

def fck_st(Grade_designation):
    if Grade_designation == 'M10':
        charact_str = 10
        standard_dev = 3.5
        fck=charact_str +1.65*standard_dev
    elif Grade_designation == 'M15':
        charact_str = 15
        standard_dev = 3.5
        fck = charact_str + 1.65 * standard_dev
    elif Grade_designation == 'M20':
        charact_str = 20
        standard_dev = 4
        fck = charact_str + 1.65 * standard_dev
    elif Grade_designation == 'M25':
        charact_str = 25
        standard_dev = 4
        fck = charact_str + 1.65 * standard_dev
    elif Grade_designation== 'M30':
        charact_str = 30
        standard_dev = 5
        fck = charact_str + 1.65 * standard_dev
    elif Grade_designation == 'M35':
        charact_str = 35
        standard_dev = 5
        fck = charact_str + 1.65 * standard_dev
    else:                              ## M40 grade of concrete
        charact_str = 40
        standard_dev = 5
        fck = charact_str + 1.65 * standard_dev
    fck=round(fck,2)

    return fck


##Ratio of volume of coarse aggregate to total volume of aggregate for different zones of fine aggregate table 3 of IS10262:2009
def Vol_CATA_ratio(Max_Nominal_size_CA,Zone):
    ## to change value on max CA size
    if Max_Nominal_size_CA == '20':

            ## to change value based on exposure condition
            if Zone == '隔爆型':
                Vol_CA_TA = 0.6
            elif Zone == '增安型':
                Vol_CA_TA = 0.62
            elif Zone == '正壓型':
                Vol_CA_TA = 0.64
            else:
                Vol_CA_TA = 0.66


    elif Max_Nominal_size_CA == '10':

            if Zone == '隔爆型':
                Vol_CA_TA = 0.44
            elif Zone == '增安型':
                Vol_CA_TA = 0.46
            elif Zone == '正壓型':
                Vol_CA_TA = 0.48
            else:
                Vol_CA_TA = 0.50


    else:
            if Zone == '隔爆型':
                Vol_CA_TA = 0.69
            elif Zone == '增安型':
                Vol_CA_TA = 0.71
            elif Zone == '正壓型':
                Vol_CA_TA = 0.73
            else:
                Vol_CA_TA = 0.75

    return Vol_CA_TA

with col13:
    Vol_Cata = Vol_CATA_ratio(Max_Nominal_size_CA,Zone)
    Vol_CA_TA=Vol_Cata
    h = str(Vol_Cata)
    h_final = st.text_input(label='Ratio of volume of CA and TA : ',value=h)#######################################################################################
#Vol_CA_TA = st.slider(value = 0.69,min_value=0.44,max_value=0.75,step=0.01,label='Volume CA to TA Factor:')

st.sidebar.subheader('材料比重 :')
Gc = st.sidebar.slider(min_value = 1.0,max_value=4.0,step = 0.01,value = 2.93,label="水泥")
Gca = st.sidebar.slider(min_value = 1.0,max_value =4.0,step = 0.01,value = 2.82,label='粗骨料')
Gcf = st.sidebar.slider(min_value = 1.0,max_value =4.0,step = 0.01,value = 2.65,label='細骨料')
Gxa = st.sidebar.slider(min_value = 1.0,max_value=4.0,step = 0.01,value = 1.121,label='混合物')
P_Air = st.sidebar.slider(min_value = 0.00,max_value =4.00,step = 0.01,value = 2.00,label='滯留空氣(%)')

buttom = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
.stButton>button {
    color: #4F8BF9;
    border-radius: 50%;
    font-size:20px;
    height: 5em;
    width: 5em;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)
co1, co2, co3 = st.beta_columns(3)
with co2:
    buttom=st.button("O👌K")
#buttom=st.button("👌")
if buttom:
    st.write('<font size="5"><center><span style="color:black;background:#DCB5FF"><b>結果 :</b></span></center></font>',unsafe_allow_html=True)
    #st.subheader('<span style="color:red;background:pink">結果:</span>',unsafe_allow_html=True)

    a=fck_st(Grade_designation)
    b=str(a)
    st.text_input(label='fck (kN/mm2)',value=b)

    ##Ratio of aggregates
    def final_computation(Workability,Max_WC_Ratio,Max_Wcontet_CAgg,Prac_WC_Ratio,reduction,Vol_CA_TA,Gxa,Gca,Gcf,Gc,P_Air):
        adopted_Wc = min(Max_WC_Ratio, Prac_WC_Ratio)  ## lesser value
        no_5_above_100 = (Workability - 50) / 25  # workability = slump value
        if Workability > 50:
            w = Max_Wcontet_CAgg + no_5_above_100 * (3 / 100) * Max_Wcontet_CAgg  ##w = water cement contentto the desirable slump
            final_water_content = ((100 - reduction) / 100) * w
        else:
            w = Workability
            final_water_content = ((100 - reduction) / 100) * w

        # Selection of cement content:
        Cement_content = final_water_content / adopted_Wc
        # After selection of zone grade
        Vol_CA_Total_Aggregate = Vol_CA_TA
        # print('Factor : {}'.format(i))

        W_C_less_by = 0.5 - adopted_Wc
        # print('W_C_less_by : {}'.format(W_C_less_by))
        Increase_by = (0.01 / 0.05) * W_C_less_by
        # print('W_C_increase_by : {}'.format(Increase_by))
        Corrected_A = Vol_CA_TA + Increase_by
        # print('Corrected wc : {}'.format(Corrected_A))
        if Method_placing == '電動':
            Total_Vol_CA = 0.9 * Corrected_A
            Vol_FA = 1 - Total_Vol_CA
            # print('Vol_CA_Pumping : {}'.format(Total_Vol_CA))
            # print('Vol_FA_Pumping : {}'.format(Vol_FA))
        else:  ## Manual Method
            Total_Vol_CA = Corrected_A
            Vol_FA = 1 - Total_Vol_CA
            # print('Vol_CA_Manual : {}'.format(Total_Vol_CA))
            # print('Vol_FA_Manual : {}'.format(Vol_FA))

        Vol_concrete = 1
        Vol_cement = (Cement_content / Gc) * (1 / 1000)
        # print('Vol_cement : {}'.format(Vol_cement))
        Vol_water = (final_water_content) * (1 / 1000)
        # print('Vol_water : {}'.format(Vol_water))
        Mass_chem_admixture = (Mass_Admixture_perc / 100) * Cement_content
        Vol_chem_admixture = (Mass_chem_admixture / Gxa) * (1 / 1000)
        # print('Vol_admixture : {}'.format(Vol_chem_admixture ))
        Vol_ALL_Aggregate = Vol_concrete - (Vol_cement + Vol_water + Vol_chem_admixture + P_Air / 100)
        Mass_CA = Vol_ALL_Aggregate * Gca * Total_Vol_CA * 1000
        Mass_FA = Vol_ALL_Aggregate * Gcf * Vol_FA * 1000

        Cement = Cement_content / 50  ## In bags
        Cement_pro = Cement_content / Cement_content
        FA_pro = Mass_FA / Cement_content
        CA_pro = Mass_CA / Cement_content

        return Cement_pro,FA_pro,CA_pro,Cement_content,final_water_content,adopted_Wc,Mass_CA,Mass_FA,Mass_chem_admixture

    ##Cement aggregate ratio:

    Cement = final_computation(Workability,Max_WC_Ratio,Max_Wcontet_CAgg,Prac_WC_Ratio,reduction,Vol_CA_TA,Gxa,Gca,Gcf,Gc,P_Air)
    Str_cement = str(Cement[0])
    Str_FA = str(round(Cement[1],1))
    Str_CA = str(round(Cement[2],1))

    Cement_bags = round(Cement[3]/50)
    Str_Cement_Content=str(round(Cement[3],3))+"  ("+str(Cement_bags)+' bags)'
    Str_Water_Content=str(round(Cement[4],3))
    Str_WC_ratio = str(Cement[5])
    Str_CA_Content=str(round(Cement[6]))
    Str_FA_Content=str(round(Cement[7]))
    Str_Admixture = str(round(Cement[8],2))

    #st.subheader('最終比例 :')
    st.write('<font size="5"><center><span style="color:black;background:#DDDDFF"><b>最終比例 :</b></span></center></font>',unsafe_allow_html=True)

    col14,col15,col16 = st.beta_columns(3)
    with col14:
        st.text_input('水泥',value=Str_cement)
    with col15:
        st.text_input('細骨料',value=Str_FA)
    with col16:
        st.text_input('粗骨料',value=Str_CA)

    #st.latex(r'''質量體積比: (kg/m^3)''')
    st.write('<font size="5"><center><span style="color:black;background:#D2E9FF"><b>質量體積比: (kg/m^3)</b></span></center></font>',unsafe_allow_html=True)
    #

    col17,col18,col19 = st.beta_columns(3)
    with col17:
        st.text_input('水泥', value=Str_Cement_Content)
    with col18:
        st.text_input('水', value=Str_Water_Content)
    with col19:
        st.text_input('比例 ', value=Str_WC_ratio)

    col20,col21,col22 = st.beta_columns(3)

    with col20:
        st.text_input('細骨料', value=Str_FA_Content)
    with col21:
        st.text_input('中骨料', value=Str_CA_Content)
    with col22:
        st.text_input('粗骨料', value=Str_Admixture)
