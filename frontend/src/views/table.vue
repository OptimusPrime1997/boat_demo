<template>
  <el-container>
    <!--<el-aside width="220px">Other msg</el-aside>-->
    <el-container>
<<<<<<< HEAD
      <el-header></el-header>
      <!--<el-header>Boat Demo</el-header>-->
      <el-main>
        <el-row :gutter="20">
          <el-col :span="17">
            <el-tabs :before-leave="clear_1" v-model="activeName2" type="card" @tab-click="handleClick" >

              <el-tab-pane  label="Tonnage Cards" name="first"   >


                <div >Tonnage offer cards</div>
                <div >
=======
      <el-header>Boat Demo</el-header>
      <el-main>
        <el-row :gutter="20">
          <el-col :span="17">
            <el-tabs v-model="activeName2" type="card" @tab-click="handleClick">
              <el-tab-pane label="Tonnage Cards" name="first">
                <div>Tonnage offer cards</div>
                <div>
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                  <!--Vessel Name 搜索框的实现-->
                  <div
                    class="search_tonnage"
                    style="text-align:left; display:inline ;float:left"
                  >
                    Vessel Name :
                    <input
                      id="searchText1"
                      type="text"
                      class="searchBox"
                      style="width:200px;height:25px;"
                    />
                  </div>

                  <!--Sender's Mail 搜索框的实现-->
                  <div
                    class="search_tonnage"
                    style="text-align:right; display:inline "
                  >
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sender's
                    Mail : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <input
<<<<<<< HEAD
                      id="senderMail1"
=======
                      id="searchMail1"
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      type="text"
                      class="searchBox"
                      style="width:200px;height:25px;"
                    />
                  </div>
                </div>

                <div>
                  <!--Open Date 日期框的实现-->
                  <div
<<<<<<< HEAD
=======
                    id="tab1_data"
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                    class="block"
                    style="text-align:left;display:inline ;float:left "
                  >
                    <span class="demonstration"
                      >Open Date : &nbsp;&nbsp;&nbsp;</span
                    >
                    <el-date-picker
                      v-model="value_a_1"
<<<<<<< HEAD
                      id="tab1_data"
                      value-format="yyyy-MM-dd"
                      type="daterange"
                      range-separator="--"
                      @change="chooseTimeRange1"
=======
                      type="daterange"
                      range-separator="--"
                      @change="changeStartTime"
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      start-placeholder="Start Date"
                      end-placeholder="End Date"
                      style="height:30px;"
                    >
                    </el-date-picker>
                  </div>

                  <!--Sent within 框的实现-->
<<<<<<< HEAD
                  <div  style="text-align:left;display:inline ">
                    &nbsp;&nbsp;Sent within : &nbsp;&nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;
                    <el-select id="sentWithin1" v-model="value_a_2" placeholder="All">
=======
                  <div style="text-align:left;display:inline ">
                    &nbsp;&nbsp;Sent within : &nbsp;&nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;
                    <el-select v-model="value_a_2" placeholder="All">
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      <el-option
                        v-for="item in options_a_2"
                        :key="item.value_a_2"
                        :label="item.label"
                        :value="item.value_a_2"
                      >
                      </el-option>
                    </el-select>
                    Days.
                  </div>
                </div>

                <div>
<<<<<<< HEAD

=======
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                  <!--Built 框的实现-->
                  <div style="text-align:left ;display:inline ;float:left">
                    Built :
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Under
<<<<<<< HEAD
                    <el-select id="built1" v-model="value_a_3" placeholder="All">
=======
                    <el-select v-model="value_a_3" placeholder="All">
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      <el-option
                        v-for="item in options_a_3"
                        :key="item.value_a_3"
                        :label="item.label"
                        :value="item.value_a_3"
                      >
                      </el-option>
                    </el-select>
                    Year(s).
                  </div>

<<<<<<< HEAD

=======
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                  <!--Mail Account 框的实现-->
                  <div style="text-align:left;display:inline ;">
                    Mail Account
                    :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<<<<<<< HEAD
                    <el-select id="mail_Account1" v-model="value_a_4" placeholder="All">
=======
                    <el-select v-model="value_a_4" placeholder="All">
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      <el-option
                        v-for="item in options_a_4"
                        :key="item.value_a_4"
                        :label="item.label"
                        :value="item.value_a_4"
                      >
                      </el-option>
                    </el-select>
                  </div>
<<<<<<< HEAD

                </div>

                <div style="height: 50px">


                  <!--DWT 框的实现-->

                  <!--<div style="text-align:left ;display:inline ;float:left">-->
                    <!--DWT-->
                    <!--:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->
                    <!--<el-select v-model="value_a_5" placeholder="All">-->
                      <!--<el-option-->
                        <!--v-for="item in options_a_5"-->
                        <!--:key="item.value_a_5"-->
                        <!--:label="item.label"-->
                        <!--:value="item.value_a_5"-->
                      <!--&gt;-->
                      <!--</el-option>-->
                    <!--</el-select>-->
                  <!--</div>-->

                  <div style="text-align:left ;display:inline ;float:left">
                    DWT :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gt(>)

                    <input
                      id="dwt1"
                      type="text"
                      class="searchBox"
                      style="width:200px;height:25px;"
                    />
                  </div>





=======
                </div>

                <div style="height: 50px">
                  <!--Built 框的实现-->
                  <div style="text-align:left ;display:inline ;float:left">
                    DWT
                    :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-select v-model="value_a_5" placeholder="All">
                      <el-option
                        v-for="item in options_a_5"
                        :key="item.value_a_5"
                        :label="item.label"
                        :value="item.value_a_5"
                      >
                      </el-option>
                    </el-select>
                  </div>

>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                  <!--&lt;!&ndash;Open Area 框的实现&ndash;&gt;-->
                  <!--<div style="text-align:left;display:inline ;" >-->
                  <!--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Open Area :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->
                  <!--<el-select v-model="value_a_6" placeholder="None">-->
                  <!--<el-option-->
                  <!--v-for="item in options_a_6"-->
                  <!--:key="item.value_a_6"-->
                  <!--:label="item.label"-->
                  <!--:value="item.value_a_6">-->
                  <!--</el-option>-->
                  <!--</el-select>-->

                  <!--</div>-->
                </div>

<<<<<<< HEAD
                <!--<button-->
                  <!--@click="searchCargoSimple1"-->
                  <!--class="btn"-->
                  <!--style="text-align:center;width:150px;height:32px;font-size:15px"-->
                <!--&gt;-->
                  <!--Search_by_One-->
                <!--</button>-->

=======
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                <button
                  @click="searchCargo1"
                  class="btn"
                  style="text-align:center;width:60px;height:32px;font-size:15px"
                >
                  Search
                </button>
<<<<<<< HEAD
                <!--<button-->
                  <!--onclick="window.location.reload();"-->
                  <!--id = 'clear_1'-->
                  <!--class="btn"-->
                  <!--style="text-align:center;width:60px;height:32px;font-size:15px"-->
                <!--&gt;-->
                  <!--Clear-->
                <!--</button>-->

=======
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e

                <el-table
                  :data="
                    tableData1.slice(
                      (currentPage - 1) * pagesize,
                      currentPage * pagesize
                    )
                  "
                  height="800"
                  border
                  style="width: 100%"
                  @row-click="display_mail"
                >
                  <el-table-column
                    prop="Vessel_name"
                    label="Vessel Name"
                    width="200"
                  >
                  </el-table-column>

                  <el-table-column prop="DWT" label="DWT" width="80">
                  </el-table-column>

<<<<<<< HEAD
                  <el-table-column id="blt1" prop="BLT" label="BLT" width="80">
=======
                  <el-table-column prop="BLT" label="BLT" width="80">
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                  </el-table-column>

                  <el-table-column
                    prop="Open_area"
                    label="Open Area"
                    width="200"
<<<<<<< HEAD
                    :formatter="deal_Open_area"
                  >
                  </el-table-column>

                  <!--实现Open_date_S和Open_date_E的合并-->
                  <el-table-column
                    label="Open Date"
                    width="200"
                    :formatter="deal_Open_Date"
                  >
                      <!--<template slot-scope="scope" >-->
                        <!--{{scope.row.Open_date_S + '&#45;&#45;'+scope.row.Open_date_E}}-->
                      <!--</template>-->
                  </el-table-column>
                  <!--<el-table-column-->
                    <!--prop="Open_date_E"-->
                    <!--label="Open Date End"-->
                    <!--width="130"-->
                  <!--&gt;-->
                  <!--</el-table-column>-->

                  <el-table-column prop="Sent" label="Sent" width="200" :formatter="deal_Sent1" >
                  </el-table-column>



                  <!--<el-table-column prop="Sent" label="Sent"  :chargNull="chargNull" width="200">-->
                  <!--</el-table-column>-->

=======
                  >
                  </el-table-column>

                  <el-table-column
                    prop="Open_date_S"
                    label="Open Date Start"
                    width="130"
                  >
                  </el-table-column>
                  <el-table-column
                    prop="Open_date_E"
                    label="Open Date End"
                    width="130"
                  >
                  </el-table-column>
                  <el-table-column prop="Sent" label="Sent" width="80">
                  </el-table-column>
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                </el-table>

                <!--&lt;!&ndash;// 处理分页&ndash;&gt;-->
                <!--<div class="yema">-->
<<<<<<< HEAD
                <!--    <el-pagination background-->
=======
                <!--    <el-pagination background-->
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                <!--@size-change="handleSizeChange"-->
                <!--@current-change="handleCurrentChange"-->
                <!--:current-page="currentPage"-->
                <!--:page-sizes="[5,10,15]"-->
                <!--:page-size="pagesize"-->
                <!--layout="total,jumper,prev, pager, next,sizes"-->
                <!--:total="tableData1.length" >-->
<<<<<<< HEAD
                <!--    </el-pagination>-->
=======
                <!--    </el-pagination>-->
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                <!--</div>-->
                <div class="yema">
                  <el-pagination
                    background
                    @size-change="handleSizeChange"
                    @current-change="handleCurrentChange"
                    :current-page="currentPage"
                    layout="prev, pager, next"
                    :total="tableData1.length"
                  >
                  </el-pagination>
                </div>
<<<<<<< HEAD

=======
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
              </el-tab-pane>

              <el-tab-pane label="Cargo Cards " name="second">
                <div>Cargo offer cards</div>
                <div>
                  <div
                    class="search_cago"
                    style="text-align:left; display:inline ;float:left"
                  >
                    Cargo Name :
                    <input
                      id="searchText2"
                      type="text"
                      class="searchBox"
                      style="width:200px;height:25px;"
                    />
                  </div>

                  <!--Sender's Mail 搜索框的实现-->
                  <div
                    class="search_tonnage"
                    style="text-align:right; display:inline "
                  >
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
<<<<<<< HEAD
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sender's
                    Mail : &nbsp;&nbsp;&nbsp;&nbsp;
                    <input
                      id="senderMail2"
=======
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sender's
                    Mail : &nbsp;&nbsp;&nbsp;&nbsp;
                    <input
                      id="searchMail2"
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      type="text"
                      class="searchBox"
                      style="width:200px;height:25px;"
                    />
                  </div>
                </div>

                <div>
                  <!--Laycan 日期框的实现-->
                  <div
<<<<<<< HEAD

=======
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                    class="block"
                    style="text-align:left;display:inline ;float:left "
                  >
                    <span class="demonstration"
<<<<<<< HEAD
                      >Laycan : &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;</span
                    >
                    <el-date-picker
                      v-model="value_b_1"
                      id="tab2_data"
                      type="daterange"
                      value-format="yyyy-MM-dd"
                      range-separator="--"
                      start-placeholder="Start Date"
                      end-placeholder="End Date"
                      @change="chooseTimeRange2"
=======
                      >Laycan : &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;</span
                    >
                    <el-date-picker
                      v-model="value_b_1"
                      type="daterange"
                      range-separator="--"
                      start-placeholder="Start Date"
                      end-placeholder="End Date"
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      style="height:30px;"
                    >
                    </el-date-picker>
                  </div>

                  <!--Sent within 框的实现-->
                  <div style="text-align:left;display:inline ">
                    &nbsp;&nbsp;Sent within : &nbsp;&nbsp; &nbsp;&nbsp;
<<<<<<< HEAD
                    <el-select id="sentWithin2" v-model="value_b_2" placeholder="All">
=======
                    <el-select v-model="value_b_2" placeholder="All">
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      <el-option
                        v-for="item in options_b_2"
                        :key="item.value_b_2"
                        :label="item.label"
                        :value="item.value_b_2"
                      >
                      </el-option>
                    </el-select>
                    Days.
                  </div>
                </div>

                <div style="height: 60px">
                  <!--&lt;!&ndash;Loding Port 框的实现&ndash;&gt;-->
                  <!--<div style="text-align:left ;display:inline ;float:left" >-->
                  <!--Loding Port : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->
                  <!--<el-select v-model="value_b_3" placeholder="All">-->
                  <!--<el-option-->
                  <!--v-for="item in options_b_3"-->
                  <!--:key="item.value_b_3"-->
                  <!--:label="item.label"-->
                  <!--:value="item.value_b_3">-->
                  <!--</el-option>-->
                  <!--</el-select>-->
                  <!---->

                  <!--</div>-->

                  <!--Mail Account 框的实现-->
                  <div style="text-align:left;display:inline ;">
<<<<<<< HEAD
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mail
                    Account :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-select id="mail_Account2" v-model="value_b_4" placeholder="All">
=======
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mail
                    Account :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-select v-model="value_b_4" placeholder="All">
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      <el-option
                        v-for="item in options_b_4"
                        :key="item.value_b_4"
                        :label="item.label"
                        :value="item.value_b_4"
                      >
                      </el-option>
                    </el-select>
                  </div>
                  <!--</div>-->
                  <!--<div>-->

                  <!--Qiantity 框的实现-->
<<<<<<< HEAD
                  <!--<div style="text-align:left ;display:inline ;float:left">-->
                    <!--Quantity :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->
                    <!--<el-select v-model="value_b_5" placeholder="All">-->
                      <!--<el-option-->
                        <!--v-for="item in options_b_5"-->
                        <!--:key="item.value_b_5"-->
                        <!--:label="item.label"-->
                        <!--:value="item.value_b_5"-->
                      <!--&gt;-->
                      <!--</el-option>-->
                    <!--</el-select>-->
                  <!--</div>-->
                  <!---->
                  <div style="text-align:left ;display:inline ;float:left">
                    Quantity :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gt(>)
                    <input
                      id="Quantity1"
                      type="text"
                      class="searchBox"
                      style="width:200px;height:25px;"
                    />
                  </div>


=======
                  <div style="text-align:left ;display:inline ;float:left">
                    Quantity :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-select v-model="value_b_5" placeholder="All">
                      <el-option
                        v-for="item in options_b_5"
                        :key="item.value_b_5"
                        :label="item.label"
                        :value="item.value_b_5"
                      >
                      </el-option>
                    </el-select>
                  </div>

>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                  <!--&lt;!&ndash;Disch. Port 框的实现&ndash;&gt;-->
                  <!--<div style="text-align:left;display:inline ;" >-->
                  <!--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Disch. Port :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->
                  <!--<el-select v-model="value_b_6" placeholder="None">-->
                  <!--<el-option-->
                  <!--v-for="item in options_b_6"-->
                  <!--:key="item.value_b_6"-->
                  <!--:label="item.label"-->
                  <!--:value="item.value_b_6">-->
                  <!--</el-option>-->
                  <!--</el-select>-->

                  <!--</div>-->
                </div>

<<<<<<< HEAD
                <!--<button-->
                  <!--@click="searchCargoSimple2"-->
                  <!--class="btn"-->
                  <!--style="text-align:center;width:160px;height:32px;font-size:15px"-->
                <!--&gt;-->
                  <!--Search_by_One-->
                <!--</button>-->

=======
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                <button
                  @click="searchCargo2"
                  class="btn"
                  style="text-align:center;width:60px;height:32px;font-size:15px"
                >
                  Search
                </button>
<<<<<<< HEAD
                <!--<button-->
                 <!--onclick="window.location.reload();"-->
                  <!--class="btn"-->
                  <!--style="text-align:center;width:60px;height:32px;font-size:15px"-->
                <!--&gt;-->
                  <!--Clear-->
                <!--</button>-->

=======
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e

                <el-table
                  :data="
                    tableData2.slice(
                      (currentPage - 1) * pagesize,
                      currentPage * pagesize
                    )
                  "
                  height="800"
                  border
                  style="width: 100%"
                  @row-click="display_mail"
                >
                  <el-table-column
                    prop="Cargo_name"
                    label="Cargo Name"
                    width="130"
<<<<<<< HEAD
                    :formatter="deal_Cargo_name"
                  >
                  </el-table-column>

                  <!--实现Quantity_s和Quantity_e的合并-->
                  <el-table-column
                    label="Quantity"
                    width="130"
                    :formatter="deal_Quantity2"
                  >
                     <!--<template slot-scope="scope">-->
                        <!--{{scope.row.Quantity_s + '-'+scope.row.Quantity_e}}-->
                      <!--</template>-->
                  </el-table-column>
                  <!--<el-table-column-->
                    <!--prop="Quantity_e"-->e
                    <!--label="Quantity_e"-->
                    <!--width="100"-->
                  <!--&gt;-->
                  <!--</el-table-column>-->
=======
                  >
                  </el-table-column>

                  <el-table-column
                    prop="Quantity_s"
                    label="Quantity_s"
                    width="100"
                  >
                  </el-table-column>
                  <el-table-column
                    prop="Quantity_e"
                    label="Quantity_e"
                    width="100"
                  >
                  </el-table-column>
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e

                  <el-table-column
                    prop="Loading_Port"
                    label="Loading Port"
<<<<<<< HEAD
                    width="150"
                    :formatter="deal_Loading_Port"
=======
                    width="130"
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                  >
                  </el-table-column>

                  <el-table-column
                    prop="Discharging_Port"
                    label="Discharging Port"
<<<<<<< HEAD
                    width="150"
                    :formatter="deal_Discharging_Port"
                  >
                  </el-table-column>

                  <!--实现LayCan_S和LayCan_E的合并-->
                  <el-table-column

                    label="LayCan"
                    width="200"
                    :formatter="deal_LayCan2"
                  >
                     <!--<template slot-scope="scope">-->
                        <!--{{scope.row.LayCan_S + '&#45;&#45;'+scope.row.LayCan_E}}-->
                      <!--</template>-->
                  </el-table-column>

                  <!--<el-table-column-->
                    <!--prop="LayCan_E"-->
                    <!--label="LayCan_End"-->
                    <!--width="120"-->
                  <!--&gt;-->
                  <!--</el-table-column>-->

                  <el-table-column prop="Sent" label="Sent" width="200" :formatter="deal_Sent2">
                  </el-table-column>

=======
                    width="140"
                  >
                  </el-table-column>

                  <el-table-column
                    prop="LayCan_S"
                    label="LayCan_Start"
                    width="120"
                  >
                  </el-table-column>
                  <el-table-column
                    prop="LayCan_E"
                    label="LayCan_End"
                    width="120"
                  >
                  </el-table-column>

                  <el-table-column prop="Sent" label="Sent" width="120">
                  </el-table-column>
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                </el-table>

                <!--&lt;!&ndash;// 处理分页&ndash;&gt;-->
                <!--<div class="yema">-->
<<<<<<< HEAD
                <!--    <el-pagination background-->
=======
                <!--    <el-pagination background-->
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                <!--@size-change="handleSizeChange"-->
                <!--@current-change="handleCurrentChange"-->
                <!--:current-page="currentPage"-->
                <!--:page-sizes="[5,10,15]"-->
                <!--:page-size="pagesize"-->
                <!--layout="total,jumper,prev, pager, next,sizes"-->
                <!--:total="tableData2.length" >-->
<<<<<<< HEAD
                <!--    </el-pagination>-->
=======
                <!--    </el-pagination>-->
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                <!--</div>-->
                <div class="yema">
                  <el-pagination
                    background
                    @size-change="handleSizeChange"
                    @current-change="handleCurrentChange"
                    :current-page="currentPage"
                    layout="prev, pager, next"
                    :total="tableData2.length"
                  >
                  </el-pagination>
                </div>
              </el-tab-pane>

              <el-tab-pane label="TC Cards" name="third">
                <div>TC offer cards</div>
                <div>
                  <div
                    class="search_cago"
                    style="text-align:left;display:inline ;float:left"
                  >
<<<<<<< HEAD
                    Account : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
=======
                    Account : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                    <input
                      id="searchText3"
                      type="text"
                      class="searchBox"
                      style="width:200px;height:25px;"
                    />
                  </div>

                  <!--Sender's Mail 搜索框的实现-->
                  <div
                    class="search_tonnage"
                    style="text-align:right; display:inline "
                  >
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sender's
                    Mail : &nbsp;&nbsp;&nbsp;&nbsp;
                    <input
<<<<<<< HEAD
                      id="senderMail3"
=======
                      id="searchMail3"
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      type="text"
                      class="searchBox"
                      style="width:200px;height:25px;"
                    />
                  </div>
                </div>

                <div>
                  <!--Laycan 日期框的实现-->
                  <div
                    class="block"
                    style="text-align:left;display:inline ;float:left "
                  >
                    <span class="demonstration"
<<<<<<< HEAD
                      >Laycan : &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;</span
                    >
                    <el-date-picker
                      v-model="value_c_1"
                      id="tab3_data"
                      value-format="yyyy-MM-dd"
=======
                      >Laycan : &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;</span
                    >
                    <el-date-picker
                      v-model="value_c_1"
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      type="daterange"
                      range-separator="--"
                      start-placeholder="Start Date"
                      end-placeholder="End Date"
<<<<<<< HEAD
                      @change="chooseTimeRange3"
=======
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      style="height:30px;"
                    >
                    </el-date-picker>
                  </div>

                  <!--Sent within 框的实现-->
                  <div style="text-align:left;display:inline ">
                    &nbsp;&nbsp;Sent within : &nbsp;&nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;
<<<<<<< HEAD
                    <el-select id="sentWithin3" v-model="value_c_2" placeholder="All">
=======
                    <el-select v-model="value_c_2" placeholder="All">
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      <el-option
                        v-for="item in options_b_2"
                        :key="item.value_c_2"
                        :label="item.label"
                        :value="item.value_c_2"
                      >
                      </el-option>
                    </el-select>
                    Days.
                  </div>
                </div>

                <div style="height: 60px">
                  <!--&lt;!&ndash;Del. Area 框的实现&ndash;&gt;-->
                  <!--<div style="text-align:left ;display:inline ;float:left" >-->
                  <!--Loding Port : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->
                  <!--<el-select v-model="value_c_3" placeholder="All">-->
                  <!--<el-option-->
                  <!--v-for="item in options_c_3"-->
                  <!--:key="item.value_c_3"-->
                  <!--:label="item.label"-->
                  <!--:value="item.value_c_3">-->
                  <!--</el-option>-->
                  <!--</el-select>-->
                  <!---->

                  <!--</div>-->

                  <!--Mail Account 框的实现-->
                  <div style="text-align:left;display:inline ;">
<<<<<<< HEAD
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mail
                    Account :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-select id="mail_Account3" v-model="value_c_4" placeholder="All">
=======
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mail
                    Account :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-select v-model="value_c_4" placeholder="All">
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                      <el-option
                        v-for="item in options_c_4"
                        :key="item.value_c_4"
                        :label="item.label"
                        :value="item.value_c_4"
                      >
                      </el-option>
                    </el-select>
                  </div>
                  <!--</div>-->
                  <!--<div>-->

                  <!--Qiantity 框的实现-->
<<<<<<< HEAD
                  <!--<div style="text-align:left ;display:inline ;float:left">-->
                    <!--Quantity :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->
                    <!--<el-select v-model="value_c_5" placeholder="All">-->
                      <!--<el-option-->
                        <!--v-for="item in options_c_5"-->
                        <!--:key="item.value_c_5"-->
                        <!--:label="item.label"-->
                        <!--:value="item.value_c_5"-->
                      <!--&gt;-->
                      <!--</el-option>-->
                    <!--</el-select>-->
                  <!--</div>-->
                    <div style="text-align:left ;display:inline ;float:left">
                    Quantity :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gt(>)

                    <input
                      id="Quantity2"
                      type="text"
                      class="searchBox"
                      style="width:200px;height:25px;"
                    />
=======
                  <div style="text-align:left ;display:inline ;float:left">
                    Quantity :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-select v-model="value_c_5" placeholder="All">
                      <el-option
                        v-for="item in options_c_5"
                        :key="item.value_c_5"
                        :label="item.label"
                        :value="item.value_c_5"
                      >
                      </el-option>
                    </el-select>
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                  </div>

                  <!--&lt;!&ndash;Redel. Area 框的实现&ndash;&gt;-->
                  <!--<div style="text-align:left;display:inline ;" >-->
                  <!--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Disch. Port :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->
                  <!--<el-select v-model="value_c_6" placeholder="None">-->
                  <!--<el-option-->
                  <!--v-for="item in options_c_6"-->
                  <!--:key="item.value_c_6"-->
                  <!--:label="item.label"-->
                  <!--:value="item.value_c_6">-->
                  <!--</el-option>-->
                  <!--</el-select>-->

                  <!--</div>-->
                </div>
<<<<<<< HEAD
                <!--<button-->
                  <!--@click="searchCargoSimple3"-->
                  <!--class="btn"-->
                  <!--style="text-align:center;width:160px;height:32px;font-size:15px"-->
                <!--&gt;-->
                  <!--Search_by_One-->
                <!--</button>-->
=======
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e

                <button
                  @click="searchCargo3"
                  class="btn"
<<<<<<< HEAD
                  style="text-align:center;width:60px;height:32px ;font-size:15px"
=======
                  style="text-align:center;width:60px;height:32px;font-size:15px"
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                >
                  Search
                </button>

<<<<<<< HEAD
                <!--<button-->
                 <!--onclick="window.location.reload();"-->
                  <!--class="btn"-->
                  <!--style="text-align:center;width:60px;height:32px;font-size:15px"-->
                <!--&gt;-->
                  <!--Clear-->
                <!--</button>-->


=======
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                <el-table
                  :data="
                    tableData3.slice(
                      (currentPage - 1) * pagesize,
                      currentPage * pagesize
                    )
                  "
                  height="800"
                  border
                  style="width: 100%"
                  @row-click="display_mail"
                >
<<<<<<< HEAD
                  <el-table-column prop="Account" label="Account" width="130":formatter="deal_Account">
                  </el-table-column>

                  <!--实现Quantity_s和Quantity_e的合并-->
                  <el-table-column
                    label="Quantity"
                    width="130"
                    :formatter="deal_Quantity3"
                  >
                     <!--<template slot-scope="scope" prop="Quantity" >-->
                        <!--{{scope.row.Quantity_s + '-'+scope.row.Quantity_e}}-->
                      <!--</template>-->
                  </el-table-column>
                  <!--<el-table-column-->
                    <!--prop="Quantity_e"-->
                    <!--label="Quantity_e"-->
                    <!--width="100"-->
                  <!--&gt;-->
                  <!--</el-table-column>-->
                  <el-table-column
                    prop="Delivery_area"
                    label="Delivery Area"
                    width="140"
                    :formatter="deal_Delivery_area"
=======
                  <el-table-column prop="Account" label="Account" width="90">
                  </el-table-column>
                  <el-table-column
                    prop="Quantity_s"
                    label="Quantity_s"
                    width="100"
                  >
                  </el-table-column>
                  <el-table-column
                    prop="Quantity_e"
                    label="Quantity_e"
                    width="100"
                  >
                  </el-table-column>
                  <el-table-column
                    prop="Delivery_area"
                    label="Delivery Area"
                    width="120"
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                  >
                  </el-table-column>
                  <el-table-column
                    prop="Redelivery_area"
                    label="Redelivery Area"
<<<<<<< HEAD
                    width="140"
                    :formatter="deal_Redelivery_area"
                  >
                  </el-table-column>

                  <!--实现LayCan_S和LayCan_E的合并-->
                  <el-table-column

                    label="LayCan"
                    width="200"
                    :formatter="deal_LayCan3"
                  >
                    <!--<template slot-scope="scope">-->
                        <!--{{scope.row.LayCan_S + '&#45;&#45;'+scope.row.LayCan_E}}-->
                      <!--</template>-->
                  </el-table-column>
                  <!--<el-table-column-->
                    <!--prop="LayCan_E"-->
                    <!--label="LayCan End"-->
                    <!--width="110"-->
                  <!--&gt;-->
                  <!--</el-table-column>-->

                  <!--实现DUR_S和DUR_E的合并-->
                  <el-table-column  label="DUR" width="90" :formatter="deal_DUR">
                    <!--<template slot-scope="scope">-->
                        <!--{{scope.row.DUR_S + '—'+scope.row.DUR_E}}-->
                      <!--</template>-->
                  </el-table-column>
                  <!--<el-table-column prop="DUR_E" label="DUR_E" width="70">-->
                  <!--</el-table-column>-->
                  <!--<el-table-column prop="Sent" label="Sent" width="130">-->
                  <!--</el-table-column>-->
                  <!--处理sent 中为0的数据不显示-->
                  <el-table-column prop="Sent" label="Sent" width="130" :formatter="deal_Sent3">
                  </el-table-column>



=======
                    width="130"
                  >
                  </el-table-column>

                  <el-table-column
                    prop="LayCan_S"
                    label="LayCan Start"
                    width="110"
                  >
                  </el-table-column>
                  <el-table-column
                    prop="LayCan_E"
                    label="LayCan End"
                    width="110"
                  >
                  </el-table-column>
                  <el-table-column prop="DUR_S" label="DUR_S" width="70">
                  </el-table-column>
                  <el-table-column prop="DUR_E" label="DUR_E" width="70">
                  </el-table-column>
                  <el-table-column prop="Sent" label="Sent" width="80">
                  </el-table-column>
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                </el-table>

                <!--&lt;!&ndash;// 处理分页&ndash;&gt;-->
                <!--<div class="yema">-->
<<<<<<< HEAD
                <!--    <el-pagination background-->
=======
                <!--    <el-pagination background-->
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                <!--@size-change="handleSizeChange"-->
                <!--@current-change="handleCurrentChange"-->
                <!--:current-page="currentPage"-->
                <!--:page-sizes="[5,10,15]"-->
                <!--:page-size="pagesize"-->
                <!--layout="total,jumper,prev, pager, next,sizes"-->
                <!--:total="tableData3.length" >-->
<<<<<<< HEAD
                <!--    </el-pagination>-->
=======
                <!--    </el-pagination>-->
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
                <!--</div>-->
                <div class="yema">
                  <el-pagination
                    background
                    @size-change="handleSizeChange"
                    @current-change="handleCurrentChange"
                    :current-page="currentPage"
                    layout="prev, pager, next"
                    :total="tableData3.length"
                  >
                  </el-pagination>
                </div>
              </el-tab-pane>
            </el-tabs>
          </el-col>

          <el-col :span="7">
            <el-tabs type="border-card">
              <el-tab-pane label="Mail">
                <!-- talbe行 点击 获取邮件方法的实现-->
                <div style="overflow-x:hidden ;height:650px">
                  <v-clamp autoresize :max-lines="10">{{ text }}</v-clamp>
                </div>
              </el-tab-pane>
              <el-tab-pane label="Memo">
                <div>
                  other msg
                </div>
              </el-tab-pane>
            </el-tabs>
          </el-col>
        </el-row>
      </el-main>
      <!--<el-footer>Footer-->
      <!--</el-footer>-->
    </el-container>
  </el-container>
</template>
<<<<<<< HEAD


<script>
import VClamp from 'vue-clamp'
export default {
  data() {



    return {
      datepickerList:[],
      cargo_dateList:[],
      tc_dateList:[],

      activeName2: 'first',
      // activeName2: 'second',
      tableData1: [],
      tableData2: [],
      tableData3: [],
      text: '',
      // //存储分页，搜索数据
      currentPage: 1,
      pagesize: 20,
      //定义Open Date日期的组件js部分
      value_a_1: '',
      //定义Sent within的组件js部分
      options_a_2: [{
        value_a_2: '选项0',
        label: 'All'
      }, {
        value_a_2: '选项1',
        label: '1'
      }, {
        value_a_2: '选项2',
        label: '2'
      }, {
        value_a_2: '选项3',
        label: '3'
      }, {
        value_a_2: '选项4',
        label: '4'
      }, {
        value_a_2: '选项5',
        label: '5'
      }, {
        value_a_2: '选项6',
        label: '6'
      }, {
        value_a_2: '选项7',
        label: '7'
      }],
      value_a_2: '',
      //定义Built的组件js部分
      options_a_3: [{
        value_a_3: '选项0',
        label: 'All'
      }, {
        value_a_3: '选项1',
        label: '5'
      }, {
        value_a_3: '选项2',
        label: '10'
      }, {
        value_a_3: '选项3',
        label: '15'
      }, {
        value_a_3: '选项4',
        label: '20'
      }, {
        value_a_3: '选项5',
        label: '25'
      }, {
        value_a_3: '选项6',
        label: '30'
      }],
      value_a_3: '',
      //定义Mail Account的组件js部分
      options_a_4: [{
        value_a_4: '选项1',
        label: 'All'
      }, {
        value_a_4: '选项2',
        label: 'mouses'
      }],
      value_a_4: '',
      //定义DWT的组件js部分
      // options_a_5: [{
      //   value_a_5: '选项1',
      //   label: 'All'
      // }, {
      //   value_a_5: '选项2',
      //   label: 'Small Handy(0-10000)'
      // }, {
      //   value_a_5: '选项3',
      //   label: 'Handy(10000-40000)'
      // }, {
      //   value_a_5: '选项4',
      //   label: 'Large Handy(35000-40000)'
      // }, {
      //   value_a_5: '选项5',
      //   label: 'Handy Max(40000-50000)'
      // }, {
      //   value_a_5: '选项6',
      //   label: 'Supra Max(40000-50000)'
      // }, {
      //   value_a_5: '选项7',
      //   label: 'Pana Max(65000-100000)'
      // }, {
      //   value_a_5: '选项8',
      //   label: 'Post PMX(90000-100000)'
      // }, {
      //   value_a_5: '选项9',
      //   label: 'Afra Max(75000-115000)'
      // }, {
      //   value_a_5: '选项10',
      //   label: 'Cape(100000-450000)'
      // }, {
      //   value_a_5: '选项11',
      //   label: 'VLCC(150000-320000)'
      // }, {
      //   value_a_5: '选项12',
      //   label: 'ULCC(320000-550000)'
      // }, {
      //   value_a_5: '选项13',
      //   label: 'Custom'
      // }],
      // value_a_5: '',
      // //定义Open Area的组件js部分
      // options_a_6: [{
      //         value_a_6: '选项1',
      //         label: 'None'
      //       }, {
      //         value_a_6: '选项2',
      //         label: '1 Days'
      //       }, {
      //         value_a_6: '选项3',
      //         label: '2 Days'
      //       }, {
      //         value_a_6: '选项4',
      //         label: '3 Days'
      //       }, {
      //         value_a_6: '选项5',
      //         label: '5 Days'
      //       }, {
      //         value_a_6: '选项6',
      //         label: '7 Days'
      //       }, {
      //         value_a_6: '选项7',
      //         label: '10 Days'
      //       }, {
      //         value_a_6: '选项8',
      //         label: '15 Days'
      //       }, ],
      // value_a_6: '',
      //定义Laycan 日期的组件js部分
      value_b_1: '',

      //定义Sent within的组件js部分
      options_b_2: [{
        value_b_2: '选项0',
        label: 'All'
      }, {
        value_b_2: '选项1',
        label: '1'
      }, {
        value_b_2: '选项2',
        label: '2'
      }, {
        value_b_2: '选项3',
        label: '3'
      }, {
        value_b_2: '选项4',
        label: '4'
      }, {
        value_b_2: '选项5',
        label: '5'
      }, {
        value_b_2: '选项6',
        label: '6'
      }, {
        value_b_2: '选项7',
        label: '7'
      }],
      value_b_2: '',
      // //定义Loding Port的组件js部分
      //  options_b_3: [{
      //          value_b_3: '选项1',
      //          label: 'None'
      //        }, {
      //          value_b_3: '选项2',
      //          label: '1 Days'
      //        }, {
      //          value_b_3: '选项3',
      //          label: '2 Days'
      //        }, {
      //          value_b_3: '选项4',
      //          label: '3 Days'
      //        }, {
      //          value_b_3: '选项5',
      //          label: '5 Days'
      //        }, {
      //          value_b_3: '选项6',
      //          label: '7 Days'
      //        }, {
      //          value_b_3: '选项7',
      //          label: '10 Days'
      //        }, {
      //          value_b_3: '选项8',
      //          label: '15 Days'
      //        },],
      //  value_b_3: '',
      //定义Mail Account的组件js部分
      options_b_4: [{
        value_b_4: '选项1',
        label: 'All'
      }, {
        value_b_4: '选项2',
        label: 'mouses'
      }],
      value_b_4: '',
      //定义Qiantity的组件js部分
      // options_b_5: [{
      //   value_b_5: '选项1',
      //   label: 'All'
      // }, {
      //   value_b_5: '选项2',
      //   label: 'Small Handy(0-10000)'
      // }, {
      //   value_b_5: '选项3',
      //   label: 'Handy(10000-40000)'
      // }, {
      //   value_b_5: '选项4',
      //   label: 'Large Handy(35000-40000)'
      // }, {
      //   value_b_5: '选项5',
      //   label: 'Handy Max(40000-50000)'
      // }, {
      //   value_b_5: '选项6',
      //   label: 'Supra Max(40000-50000)'
      // }, {
      //   value_b_5: '选项7',
      //   label: 'Pana Max(65000-100000)'
      // }, {
      //   value_b_5: '选项8',
      //   label: 'Post PMX(90000-100000)'
      // }, {
      //   value_b_5: '选项9',
      //   label: 'Afra Max(75000-115000)'
      // }, {
      //   value_b_5: '选项10',
      //   label: 'Cape(100000-450000)'
      // }, {
      //   value_b_5: '选项11',
      //   label: 'VLCC(150000-320000)'
      // }, {
      //   value_b_5: '选项12',
      //   label: 'ULCC(320000-550000)'
      // }, {
      //   value_b_5: '选项13',
      //   label: 'Custom'
      // }],
      // value_b_5: '',
      // //定义Disch. Port的组件js部分
      // options_b_6: [{
      //         value_b_6: '选项1',
      //         label: 'None'
      //       }, {
      //         value_b_6: '选项2',
      //         label: '1 Days'
      //       }, {
      //         value_b_6: '选项3',
      //         label: '2 Days'
      //       }, {
      //         value_b_6: '选项4',
      //         label: '3 Days'
      //       }, {
      //         value_b_6: '选项5',
      //         label: '5 Days'
      //       }, {
      //         value_b_6: '选项6',
      //         label: '7 Days'
      //       }, {
      //         value_b_6: '选项7',
      //         label: '10 Days'
      //       }, {
      //         value_b_6: '选项8',
      //         label: '15 Days'
      //       }, ],
      // value_b_6: '',
      //定义Laycan 日期的组件js部分
      value_c_1: '',

      //定义Sent within的组件js部分
      options_c_2: [{
        value_c_2: '选项0',
        label: 'All'
      }, {
        value_c_2: '选项1',
        label: '1'
      }, {
        value_c_2: '选项2',
        label: '2'
      }, {
        value_c_2: '选项3',
        label: '3'
      }, {
        value_c_2: '选项4',
        label: '4'
      }, {
        value_c_2: '选项5',
        label: '5'
      }, {
        value_c_2: '选项6',
        label: '6'
      }, {
        value_c_2: '选项7',
        label: '7'
      }],
      value_c_2: '',
      // //定义Loding Port的组件js部分
      //  options_c_3: [{
      //          value_c_3: '选项1',
      //          label: 'None'
      //        }, {
      //          value_c_3: '选项2',
      //          label: '1 Days'
      //        }, {
      //          value_c_3: '选项3',
      //          label: '2 Days'
      //        }, {
      //          value_c_3: '选项4',
      //          label: '3 Days'
      //        }, {
      //          value_c_3: '选项5',
      //          label: '5 Days'
      //        }, {
      //          value_c_3: '选项6',
      //          label: '7 Days'
      //        }, {
      //          value_c_3: '选项7',
      //          label: '10 Days'
      //        }, {
      //          value_c_3: '选项8',
      //          label: '15 Days'
      //        },],
      //  value_c_3: '',
      //定义Mail Account的组件js部分
      options_c_4: [{
        value_c_4: '选项1',
        label: 'All'
      }, {
        value_c_4: '选项2',
        label: 'mouses'
      }],
      value_c_4: '',
      // //定义Qiantity的组件js部分
      // options_c_5: [{
      //   value_c_5: '选项1',
      //   label: 'All'
      // }, {
      //   value_c_5: '选项2',
      //   label: 'Small Handy(0-10000)'
      // }, {
      //   value_c_5: '选项3',
      //   label: 'Handy(10000-40000)'
      // }, {
      //   value_c_5: '选项4',
      //   label: 'Large Handy(35000-40000)'
      // }, {
      //   value_c_5: '选项5',
      //   label: 'Handy Max(40000-50000)'
      // }, {
      //   value_c_5: '选项6',
      //   label: 'Supra Max(40000-50000)'
      // }, {
      //   value_c_5: '选项7',
      //   label: 'Pana Max(65000-100000)'
      // }, {
      //   value_c_5: '选项8',
      //   label: 'Post PMX(90000-100000)'
      // }, {
      //   value_c_5: '选项9',
      //   label: 'Afra Max(75000-115000)'
      // }, {
      //   value_c_5: '选项10',
      //   label: 'Cape(100000-450000)'
      // }, {
      //   value_c_5: '选项11',
      //   label: 'VLCC(150000-320000)'
      // }, {
      //   value_c_5: '选项12',
      //   label: 'ULCC(320000-550000)'
      // }, {
      //   value_c_5: '选项13',
      //   label: 'Custom'
      // }],
      // value_c_5: '',
      // //定义Disch. Port的组件js部分
      // options_c_6: [{
      //         value_c_6: '选项1',
      //         label: 'None'
      //       }, {
      //         value_c_6: '选项2',
      //         label: '1 Days'
      //       }, {
      //         value_c_6: '选项3',
      //         label: '2 Days'
      //       }, {
      //         value_c_6: '选项4',
      //         label: '3 Days'
      //       }, {
      //         value_c_6: '选项5',
      //         label: '5 Days'
      //       }, {
      //         value_c_6: '选项6',
      //         label: '7 Days'
      //       }, {
      //         value_c_6: '选项7',
      //         label: '10 Days'
      //       }, {
      //         value_c_6: '选项8',
      //         label: '15 Days'
      //       }, ],
      // value_c_6: '',
    };

  },
  mounted() {
    var self = this;
    // var tableData2 = new Array();
    this.axios({
      method: "get",
      url: "http://127.0.0.1:8888/users/cargo"
    })
      .then(function (response) {
        var a = eval(response.data);
        for (var i = 0; i < a.list.length; i++) {
          self.tableData2.push(a.list[i].fields);
          //JSON.stringify(a.list[i].fields)
        }
        console.log("tableData2")
        console.log(self.tableData2);
        //this.tableData1.splice(xxx,xxx,xxx);
      })
      .catch(function (error) {
        console.log(error);
      });
    // var tableData1 = new Array();
    this.axios({
      method: "get",
      url: "http://127.0.0.1:8888/users/tonnage"
    })
      .then(function (response) {
        var a = eval(response.data);
        for (var i = 0; i < a.list.length; i++) {
          self.tableData1.push(a.list[i].fields);
          //JSON.stringify(a.list[i].fields)
        }
        console.log("tableData1")
        console.log(self.tableData1);
        //this.tableData1.splice(xxx,xxx,xxx);
      })
      .catch(function (error) {
        console.log(error);
      });
    // var tableData3 = new Array();
    this.axios({
      method: "get",
      url: "http://127.0.0.1:8888/users/tc"
    })
      .then(function (response) {
        var a = eval(response.data);
        for (var i = 0; i < a.list.length; i++) {
          self.tableData3.push(a.list[i].fields);
          //JSON.stringify(a.list[i].fields)
        }
        console.log("tableData3")
        console.log(self.tableData3);
        //this.tableData1.splice(xxx,xxx,xxx);
      })
      .catch(function (error) {
        console.log(error);
      });
    // console.log("test");
    // console.log("test");
  },



  methods: {

    // reflush(){
    //   window.location.reload(true);
    //
    // },
    clear_1(tab, event){

        if(tab == 'first'){
          //将第一页的tab内容清空
          // var obj = document.getElementById('searchText1') ;
          // obj.outerHTML=obj.outerHTML;
          // var obj2 = document.getElementById('dwt1') ;
          // obj2.outerHTML=obj2.outerHTML;
          // var obj3 = document.getElementById('senderMail1') ;
          // obj3.outerHTML=obj3.outerHTML;
          // var obj4 = document.getElementById('sentWithin1') ;
          // this.value_a_2 = [ ];
          // var obj5 = document.getElementById('tab1_data') ;
          // this.value_a_1 = [ ];
          // var obj6 = document.getElementById('built1') ;
          // this.value_a_3 = [ ];
          // var obj7 = document.getElementById('mail_Account1') ;
          // this.value_a_4 = [ ];
          window.location.reload(true);

          }
          if(tab == 'second'){
            //将第二页的tab内容清空
           var obj = document.getElementById('searchText2');
           obj.outerHTML = obj.outerHTML;
           var obj2 = document.getElementById('Quantity1');
           obj2.outerHTML=obj2.outerHTML;
           var obj3 = document.getElementById('senderMail2') ;
           obj3.outerHTML=obj3.outerHTML;
           var obj4 = document.getElementById('sentWithin2') ;
           this.value_b_2 = [ ];
           var obj5 = document.getElementById('tab2_data') ;
           this.value_b_1 = [ ];
           var obj6 = document.getElementById('mail_Account2') ;
           this.value_b_4 = [ ];

        }
         if(tab == 'third'){
           //将第三页的tab内容清空
           var obj = document.getElementById('searchText3');
           obj.outerHTML = obj.outerHTML;
           var obj2 = document.getElementById('Quantity2');
           obj2.outerHTML=obj2.outerHTML;
           var obj3 = document.getElementById('senderMail3') ;
           obj3.outerHTML=obj3.outerHTML;
           var obj4 = document.getElementById('sentWithin3') ;
           this.value_c_2 = [ ];
           var obj5 = document.getElementById('tab3_data') ;
           this.value_c_1 = [ ];
           var obj6 = document.getElementById('mail_Account3') ;
           this.value_c_4 = [ ];

        }

    },



    //对 tableDate3中的空数据和标识数据进行处理
    //将sent 中 0转换为空
    deal_Sent3(row, column) {
      if(row.Sent.valueOf()==0){
          return '';
      }
        return row.Sent;
    },

    //将Delivery_area 中 标识string转换为空
    deal_Delivery_area(row, column) {
      if(row.Delivery_area.valueOf()=='no dely match'){
          return '';
      }
      if(row.Delivery_area.valueOf()=='none dely match'){
          return '';
      }
      if(row.Delivery_area.valueOf()=='no delivery area match'){
          return '';
      }
        return row.Delivery_area;
    },
    //将Redelivery_area 中 标识string转换为空
    deal_Redelivery_area(row, column) {
      if(row.Redelivery_area.valueOf()=='No redely match'){
          return '';
      }
      if(row.Redelivery_area.valueOf()=='none redely match'){
          return '';
      }
      if(row.Redelivery_area.valueOf()=='no redelivery area match'){
          return '';
      }
        return row.Redelivery_area;
    },
    //将Account 中 标识string转换为空
    deal_Account(row, column) {
      if(row.Account.valueOf()=='no account match'){
          return '';
      }

        return row.Account;
    },
    //将Quantity 中 标识string转换为空
    deal_Quantity3(row, column) {
     if(row.Quantity_s+'--'+row.Quantity_e.valueOf()=='0--0'){
        return '';
    }
    return row.Quantity_s+'--'+row.Quantity_e;
    },
    //将LayCan 中 标识sting转换为空
    deal_LayCan3(row, column) {
      if(row.LayCan_S+'--'+row.LayCan_E.valueOf()=='1900-01-01--1900-01-01'){
          return '';
      }
        return row.LayCan_S+'--'+row.LayCan_E;
    },
    //将DUR中 标识sting转换为空
    deal_DUR(row, column) {
      if(row.DUR_S+'--'+row.DUR_E.valueOf()=='0--0'){
          return '';
      }
        return row.DUR_S+'--'+row.DUR_E;
    },

    //对 tableDate2中的空数据和标识数据进行处理
    //将Cargo_name 中 标识string转换为空
    deal_Cargo_name(row, column) {
      if(row.Cargo_name.valueOf()=='none item name match'){
          return '';
      }

        return row.Cargo_name;
    },
    //将Loading_Port 中 标识string转换为空
    deal_Loading_Port(row, column) {
      if(row.Loading_Port.valueOf()=='no loading port match'){
          return '';
      }
        return row.Loading_Port;
    },
    //将Discharging_Port 中 标识string转换为空
    deal_Discharging_Port(row, column) {
      if(row.Discharging_Port.valueOf()=='no discharging port match'){
          return '';
      }
        return row.Discharging_Port;
    },
    //将Sent 中 标识0转换为空
    deal_Sent2(row, column) {
      if(row.Sent.valueOf()==0){
          return '';
      }
        return row.Sent;
    },
    //将Quantity 中 标识string转换为空
    deal_Quantity2(row, column) {
     if(row.Quantity_s+'--'+row.Quantity_e.valueOf()=='0--0'){
        return '';
    }
    return row.Quantity_s+'--'+row.Quantity_e;
    },
    //将LayCan 中 标识sting转换为空
    deal_LayCan2(row, column) {
      if(row.LayCan_S+'--'+row.LayCan_E.valueOf()=='1900-01-01--1900-01-01'){
          return '';
      }
        return row.LayCan_S+'--'+row.LayCan_E;
    },

    // 对 tableDate1中的空数据和标识数据进行处理
    //将Sent 中 标识0转换为空
    deal_Sent1(row, column) {
      if(row.Sent.valueOf()==0){
          return '';
      }
        return row.Sent;
    },
    //将Open_area 中 标识sting转换为空
    deal_Open_area(row, column) {
      if(row.Open_area.valueOf()=='no open area match'){
          return '';
      }
        return row.Open_area;
    },
    //将Open_Date 中 标识sting转换为空
    deal_Open_Date(row, column) {
      if(row.Open_date_S+'--'+row.Open_date_E.valueOf()=='1900-01-01--1900-01-01'){
          return '';
      }
        return row.Open_date_S+'--'+row.Open_date_E;
    },



    // 将日期显示为yyyy-mm-dd
    //  chooseTimeRange(t) {
    //   console.log(t);//结果为一个数组，如：["2018-08-04", "2018-08-06"]
    // },
    chooseTimeRange1(t) {
      this.datepickerList.splice(0,this.datepickerList.length);
       for(var i=0;i<t.length;i++){
         this.datepickerList.push(t[i]);
       }
      console.log(this.datepickerList);//结果为一个数组，如：["2018-08-04", "2018-08-06"]
    },
    chooseTimeRange2(t) {
      this.cargo_dateList.splice(0,this.cargo_dateList.length);
       for(var i=0;i<t.length;i++){
         this.cargo_dateList.push(t[i]);
       }
      console.log(this.cargo_dateList);//结果为一个数组，如：["2018-08-04", "2018-08-06"]
    },
    chooseTimeRange3(t) {
      this.tc_dateList.splice(0,this.tc_dateList.length);
       for(var i=0;i<t.length;i++){
         this.tc_dateList.push(t[i]);
       }
      console.log(this.tc_dateList);//结果为一个数组，如：["2018-08-04", "2018-08-06"]
    },

    // tonnage talbe行 点击方法
    display_mail(row) {
      // console.log("display mail method");
      // console.log(row['mail_text']);
      this.text = row['mail_text']
    },
    ///处理分页 初始页currentPage、初始每页数据数pagesize和数据tableDate1,tableDate2,tableDate3
    handleSizeChange: function (size) {
      this.pagesize = size;
    },
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage;
    },
    // 搜素框方法
    // searchCargoSimple1(){
    //    var self = this;
    //       this.tableData1.splice(0, this.tableData1.length);
    //       var data1 = new Array();
    //       var searchText1 = document.getElementById("searchText1").value;
    //       console.log(searchText1);
    //       //console.log(searchText.text);
    //
    //         this.axios({
    //           method: "get",
    //           url: "http://127.0.0.1:8888/users/search_tonnage/" + searchText1,
    //         })
    //           .then(function (response) {
    //
    //             console.log("axios method");
    //             console.log(response);
    //             console.log(eval(response.data));
    //             // self.tableData1.splice(0, tableData1.length);
    //             var a = eval(response.data);
    //             for (var i = 0; i < a.list.length; i++) {
    //               self.tableData1.push(a.list[i].fields);
    //               //JSON.stringify(a.list[i].fields)
    //             }
    //             //console.log(data2);
    //             //this.tableData1.splice(xxx,xxx,xxx);
    //           }
    //
    //           )
    //           .catch(function (error) {
    //             console.log(error);
    //           });
    //         return data1;
    //
    // },

    searchCargo1() {
      console.log("datePickerList");
      console.log(this.datepickerList);

      var self = this;
      this.tableData1.splice(0, this.tableData1.length);
      var data1 = new Array();

      if (searchText1 = document.getElementById("searchText1").value){
          var searchText1 = document.getElementById("searchText1").value;
      }else{
        searchText1=''
      }

      // var searchText1 = document.getElementById("searchText1").value;
      console.log(searchText1);
      //console.log(searchText.text);
      var tab1_data = document.getElementById("tab1_data");

      // tab1_data.datepickerList

      if(this.datepickerList[0]){
        var data_s = this.datepickerList[0];
        var data_e = this.datepickerList[1];
      }else{
        data_s="1990-03-02";
        data_e="3000-03-02";
      }

      if (document.getElementById("dwt1").value){
        var dwt1 = document.getElementById("dwt1").value;
      }else{
        dwt1=0
      }

      var conditions = {
        "vessel_name": searchText1,
        // "vessel_name": "A",
        "sender_mail": "0",
        //   "opendate_start": "2018-03-02",
        // "opendate_end": "2018-03-09",
        "opendate_start": data_s,
        "opendate_end": data_e,
        "days": 1,
        "built": 100,
        "account": "",
        "dwt": dwt1
      }


      this.axios({
        method: "post",
        url: "http://127.0.0.1:8888/users/tonnage_search",
        data:conditions
      })
        .then(function (response) {

          console.log("axios method");
          console.log(response);
          console.log(eval(response.data));
          // self.tableData1.splice(0, tableData1.length);
          var a = eval(response.data);
          for (var i = 0; i < a.list.length; i++) {
            self.tableData1.push(a.list[i].fields);
            //JSON.stringify(a.list[i].fields)
          }
          //console.log(data2);
          //this.tableData1.splice(xxx,xxx,xxx);
        }

        )
        .catch(function (error) {
          console.log(error);
        });
      return data1;

    },
     // searchCargoSimple2() {
     //      var self = this;
     //      this.tableData2.splice(0, this.tableData2.length);
     //      var data2 = new Array();
     //      var searchText2 = document.getElementById("searchText2").value;
     //      console.log(searchText2);
     //      //console.log(searchText.text);
     //      this.axios({
     //        method: "get",
     //        url: "http://127.0.0.1:8888/users/search_cargo/" + searchText2,
     //      })
     //        .then(function (response) {
     //          console.log("axios method");
     //          console.log(response);
     //          console.log(eval(response.data));
     //          // self.tableData2.splice(0, tableData2.length);
     //          var a = eval(response.data);
     //          for (var i = 0; i < a.list.length; i++) {
     //            self.tableData2.push(a.list[i].fields);
     //            //JSON.stringify(a.list[i].fields)
     //          }
     //          //console.log(data2);
     //          //this.tableData1.splice(xxx,xxx,xxx);
     //        })
     //        .catch(function (error) {
     //          console.log(error);
     //        });
     //      return data2;
     //    },
    searchCargo2() {

      var self = this;
      this.tableData2.splice(0, this.tableData2.length);
      var data2 = new Array();
      // var searchText2 = document.getElementById("searchText2").value;
      if (searchText2 = document.getElementById("searchText2").value){
          var searchText2 = document.getElementById("searchText2").value;
      }else{
        searchText2=''
      }

      console.log("LLLLLLLLL");
      console.log(searchText2);
      //console.log(searchText.text);
      var tab2_data = document.getElementById("tab2_data");




      if(this.cargo_dateList[0]){
      var data_s = this.cargo_dateList[0];
      var data_e = this.cargo_dateList[1];
      }else{
        data_s="1990-03-02";
        data_e="3000-03-02";
      }

      if (document.getElementById("Quantity1").value){
        var Quantity1 = document.getElementById("Quantity1").value;
      }else{
        Quantity1=0
      }

      var conditions = {
        "cargo_name": searchText2,
        "sender_mail": "0",
        // "laycan_start": "2018-03-20",
        // "laycan_end": "2019-03-31",
        "laycan_start": data_s,
        "laycan_end": data_e,
        "days": 1,
        "quantity": Quantity1,
        "account": ""
=======
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e

      }

<<<<<<< HEAD
      this.axios({
        method: "post",
        url: "http://127.0.0.1:8888/users/cargo_search",
=======
<script>
import VClamp from 'vue-clamp'
export default {
  data() {
    return {
      activeName2: 'first',
      tableData1: [],
      tableData2: [],
      tableData3: [],
      text: '',

      // //存储分页，搜索数据
      currentPage: 1,
      pagesize: 20,

      //定义Open Date日期的组件js部分
      value_a_1: '',

      //定义Sent within的组件js部分
      options_a_2: [{
        value_a_2: '选项0',
        label: 'All'
      }, {
        value_a_2: '选项1',
        label: '1'
      }, {
        value_a_2: '选项2',
        label: '2'
      }, {
        value_a_2: '选项3',
        label: '3'
      }, {
        value_a_2: '选项4',
        label: '4'
      }, {
        value_a_2: '选项5',
        label: '5'
      }, {
        value_a_2: '选项6',
        label: '6'
      }, {
        value_a_2: '选项7',
        label: '7'
      }],
      value_a_2: '',

      //定义Built的组件js部分
      options_a_3: [{
        value_a_3: '选项0',
        label: 'All'
      }, {
        value_a_3: '选项1',
        label: '5'
      }, {
        value_a_3: '选项2',
        label: '10'
      }, {
        value_a_3: '选项3',
        label: '15'
      }, {
        value_a_3: '选项4',
        label: '20'
      }, {
        value_a_3: '选项5',
        label: '25'
      }, {
        value_a_3: '选项6',
        label: '30'
      }],
      value_a_3: '',

      //定义Mail Account的组件js部分
      options_a_4: [{
        value_a_4: '选项1',
        label: 'All'
      }, {
        value_a_4: '选项2',
        label: 'mouses'
      }],
      value_a_4: '',

      //定义DWT的组件js部分
      options_a_5: [{
        value_a_5: '选项1',
        label: 'All'
      }, {
        value_a_5: '选项2',
        label: 'Small Handy(0-10000)'
      }, {
        value_a_5: '选项3',
        label: 'Handy(10000-40000)'
      }, {
        value_a_5: '选项4',
        label: 'Large Handy(35000-40000)'
      }, {
        value_a_5: '选项5',
        label: 'Handy Max(40000-50000)'
      }, {
        value_a_5: '选项6',
        label: 'Supra Max(40000-50000)'
      }, {
        value_a_5: '选项7',
        label: 'Pana Max(65000-100000)'
      }, {
        value_a_5: '选项8',
        label: 'Post PMX(90000-100000)'
      }, {
        value_a_5: '选项9',
        label: 'Afra Max(75000-115000)'
      }, {
        value_a_5: '选项10',
        label: 'Cape(100000-450000)'
      }, {
        value_a_5: '选项11',
        label: 'VLCC(150000-320000)'
      }, {
        value_a_5: '选项12',
        label: 'ULCC(320000-550000)'
      }, {
        value_a_5: '选项13',
        label: 'Custom'
      }],
      value_a_5: '',
      // //定义Open Area的组件js部分
      // options_a_6: [{
      //         value_a_6: '选项1',
      //         label: 'None'
      //       }, {
      //         value_a_6: '选项2',
      //         label: '1 Days'
      //       }, {
      //         value_a_6: '选项3',
      //         label: '2 Days'
      //       }, {
      //         value_a_6: '选项4',
      //         label: '3 Days'
      //       }, {
      //         value_a_6: '选项5',
      //         label: '5 Days'
      //       }, {
      //         value_a_6: '选项6',
      //         label: '7 Days'
      //       }, {
      //         value_a_6: '选项7',
      //         label: '10 Days'
      //       }, {
      //         value_a_6: '选项8',
      //         label: '15 Days'
      //       }, ],
      // value_a_6: '',

      //定义Laycan 日期的组件js部分
      value_b_1: '',

      //定义Sent within的组件js部分
      options_b_2: [{
        value_b_2: '选项0',
        label: 'All'
      }, {
        value_b_2: '选项1',
        label: '1'
      }, {
        value_b_2: '选项2',
        label: '2'
      }, {
        value_b_2: '选项3',
        label: '3'
      }, {
        value_b_2: '选项4',
        label: '4'
      }, {
        value_b_2: '选项5',
        label: '5'
      }, {
        value_b_2: '选项6',
        label: '6'
      }, {
        value_b_2: '选项7',
        label: '7'
      }],
      value_b_2: '',

      // //定义Loding Port的组件js部分
      //  options_b_3: [{
      //          value_b_3: '选项1',
      //          label: 'None'
      //        }, {
      //          value_b_3: '选项2',
      //          label: '1 Days'
      //        }, {
      //          value_b_3: '选项3',
      //          label: '2 Days'
      //        }, {
      //          value_b_3: '选项4',
      //          label: '3 Days'
      //        }, {
      //          value_b_3: '选项5',
      //          label: '5 Days'
      //        }, {
      //          value_b_3: '选项6',
      //          label: '7 Days'
      //        }, {
      //          value_b_3: '选项7',
      //          label: '10 Days'
      //        }, {
      //          value_b_3: '选项8',
      //          label: '15 Days'
      //        },],
      //  value_b_3: '',

      //定义Mail Account的组件js部分
      options_b_4: [{
        value_b_4: '选项1',
        label: 'All'
      }, {
        value_b_4: '选项2',
        label: 'mouses'
      }],
      value_b_4: '',

      //定义Qiantity的组件js部分
      options_b_5: [{
        value_b_5: '选项1',
        label: 'All'
      }, {
        value_b_5: '选项2',
        label: 'Small Handy(0-10000)'
      }, {
        value_b_5: '选项3',
        label: 'Handy(10000-40000)'
      }, {
        value_b_5: '选项4',
        label: 'Large Handy(35000-40000)'
      }, {
        value_b_5: '选项5',
        label: 'Handy Max(40000-50000)'
      }, {
        value_b_5: '选项6',
        label: 'Supra Max(40000-50000)'
      }, {
        value_b_5: '选项7',
        label: 'Pana Max(65000-100000)'
      }, {
        value_b_5: '选项8',
        label: 'Post PMX(90000-100000)'
      }, {
        value_b_5: '选项9',
        label: 'Afra Max(75000-115000)'
      }, {
        value_b_5: '选项10',
        label: 'Cape(100000-450000)'
      }, {
        value_b_5: '选项11',
        label: 'VLCC(150000-320000)'
      }, {
        value_b_5: '选项12',
        label: 'ULCC(320000-550000)'
      }, {
        value_b_5: '选项13',
        label: 'Custom'
      }],
      value_b_5: '',
      // //定义Disch. Port的组件js部分
      // options_b_6: [{
      //         value_b_6: '选项1',
      //         label: 'None'
      //       }, {
      //         value_b_6: '选项2',
      //         label: '1 Days'
      //       }, {
      //         value_b_6: '选项3',
      //         label: '2 Days'
      //       }, {
      //         value_b_6: '选项4',
      //         label: '3 Days'
      //       }, {
      //         value_b_6: '选项5',
      //         label: '5 Days'
      //       }, {
      //         value_b_6: '选项6',
      //         label: '7 Days'
      //       }, {
      //         value_b_6: '选项7',
      //         label: '10 Days'
      //       }, {
      //         value_b_6: '选项8',
      //         label: '15 Days'
      //       }, ],
      // value_b_6: '',

      //定义Laycan 日期的组件js部分
      value_c_1: '',

      //定义Sent within的组件js部分
      options_c_2: [{
        value_c_2: '选项0',
        label: 'All'
      }, {
        value_c_2: '选项1',
        label: '1'
      }, {
        value_c_2: '选项2',
        label: '2'
      }, {
        value_c_2: '选项3',
        label: '3'
      }, {
        value_c_2: '选项4',
        label: '4'
      }, {
        value_c_2: '选项5',
        label: '5'
      }, {
        value_c_2: '选项6',
        label: '6'
      }, {
        value_c_2: '选项7',
        label: '7'
      }],
      value_c_2: '',

      // //定义Loding Port的组件js部分
      //  options_c_3: [{
      //          value_c_3: '选项1',
      //          label: 'None'
      //        }, {
      //          value_c_3: '选项2',
      //          label: '1 Days'
      //        }, {
      //          value_c_3: '选项3',
      //          label: '2 Days'
      //        }, {
      //          value_c_3: '选项4',
      //          label: '3 Days'
      //        }, {
      //          value_c_3: '选项5',
      //          label: '5 Days'
      //        }, {
      //          value_c_3: '选项6',
      //          label: '7 Days'
      //        }, {
      //          value_c_3: '选项7',
      //          label: '10 Days'
      //        }, {
      //          value_c_3: '选项8',
      //          label: '15 Days'
      //        },],
      //  value_c_3: '',

      //定义Mail Account的组件js部分
      options_c_4: [{
        value_c_4: '选项1',
        label: 'All'
      }, {
        value_c_4: '选项2',
        label: 'mouses'
      }],
      value_c_4: '',

      //定义Qiantity的组件js部分
      options_c_5: [{
        value_c_5: '选项1',
        label: 'All'
      }, {
        value_c_5: '选项2',
        label: 'Small Handy(0-10000)'
      }, {
        value_c_5: '选项3',
        label: 'Handy(10000-40000)'
      }, {
        value_c_5: '选项4',
        label: 'Large Handy(35000-40000)'
      }, {
        value_c_5: '选项5',
        label: 'Handy Max(40000-50000)'
      }, {
        value_c_5: '选项6',
        label: 'Supra Max(40000-50000)'
      }, {
        value_c_5: '选项7',
        label: 'Pana Max(65000-100000)'
      }, {
        value_c_5: '选项8',
        label: 'Post PMX(90000-100000)'
      }, {
        value_c_5: '选项9',
        label: 'Afra Max(75000-115000)'
      }, {
        value_c_5: '选项10',
        label: 'Cape(100000-450000)'
      }, {
        value_c_5: '选项11',
        label: 'VLCC(150000-320000)'
      }, {
        value_c_5: '选项12',
        label: 'ULCC(320000-550000)'
      }, {
        value_c_5: '选项13',
        label: 'Custom'
      }],
      value_c_5: '',
      // //定义Disch. Port的组件js部分
      // options_c_6: [{
      //         value_c_6: '选项1',
      //         label: 'None'
      //       }, {
      //         value_c_6: '选项2',
      //         label: '1 Days'
      //       }, {
      //         value_c_6: '选项3',
      //         label: '2 Days'
      //       }, {
      //         value_c_6: '选项4',
      //         label: '3 Days'
      //       }, {
      //         value_c_6: '选项5',
      //         label: '5 Days'
      //       }, {
      //         value_c_6: '选项6',
      //         label: '7 Days'
      //       }, {
      //         value_c_6: '选项7',
      //         label: '10 Days'
      //       }, {
      //         value_c_6: '选项8',
      //         label: '15 Days'
      //       }, ],
      // value_c_6: '',




    };
  },



  mounted() {
    var self = this;
    // var tableData2 = new Array();
    this.axios({
      method: "get",
      url: "http://127.0.0.1:8888/users/cargo"
    })
      .then(function (response) {
        var a = eval(response.data);
        for (var i = 0; i < a.list.length; i++) {
          self.tableData2.push(a.list[i].fields);
          //JSON.stringify(a.list[i].fields)
        }
        console.log("tableData2")
        console.log(self.tableData2);
        //this.tableData1.splice(xxx,xxx,xxx);
      })
      .catch(function (error) {
        console.log(error);
      });
    // var tableData1 = new Array();

    this.axios({
      method: "get",
      url: "http://127.0.0.1:8888/users/tonnage"
    })
      .then(function (response) {
        var a = eval(response.data);
        for (var i = 0; i < a.list.length; i++) {
          self.tableData1.push(a.list[i].fields);
          //JSON.stringify(a.list[i].fields)
        }
        console.log("tableData1")
        console.log(self.tableData1);
        //this.tableData1.splice(xxx,xxx,xxx);
      })
      .catch(function (error) {
        console.log(error);
      });
    // var tableData3 = new Array();
    this.axios({
      method: "get",
      url: "http://127.0.0.1:8888/users/tc"
    })
      .then(function (response) {
        var a = eval(response.data);
        for (var i = 0; i < a.list.length; i++) {
          self.tableData3.push(a.list[i].fields);
          //JSON.stringify(a.list[i].fields)
        }
        console.log("tableData3")
        console.log(self.tableData3);
        //this.tableData1.splice(xxx,xxx,xxx);
      })
      .catch(function (error) {
        console.log(error);
      });
    // console.log("test");
    // console.log("test");
  },
  methods: {
    // 将日期显示为yyyy-mm-dd
    changeStartTime(time) {
      console.log('starttime', time);
      this.formdata2.travelStartTime = time;
    },
    // tonnage talbe行 点击方法
    display_mail(row) {
      // console.log("display mail method");
      // console.log(row['mail_text']);
      this.text = row['mail_text']

    },

    ///处理分页 初始页currentPage、初始每页数据数pagesize和数据tableDate1,tableDate2,tableDate3
    handleSizeChange: function (size) {
      this.pagesize = size;
    },
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage;
    },


    // 搜素框方法
    searchCargo1() {
      var self = this;
      this.tableData1.splice(0, this.tableData1.length);
      var data1 = new Array();
      var searchText1 = document.getElementById("searchText1").value;
      console.log(searchText1);
      //console.log(searchText.text);
      var conditions = {
        "vessel_name": "PACIFIC",
        "sender_mail": "0",
        "opendate_start": "2018-03-02",
        "opendate_end": "2018-03-09",
        "days": 1,
        "built": 100,
        "account": "",
        "dwt": 0
      }
      this.axios({
        method: "post",
        url: "http://127.0.0.1:8888/users/tonnage_search",
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
        data:conditions
      })
        .then(function (response) {
          console.log("axios method");
          console.log(response);
          console.log(eval(response.data));
<<<<<<< HEAD
          // self.tableData1.splice(0, tableData2.length);
=======
          // self.tableData1.splice(0, tableData1.length);
          var a = eval(response.data);
          for (var i = 0; i < a.list.length; i++) {
            self.tableData1.push(a.list[i].fields);
            //JSON.stringify(a.list[i].fields)
          }
          //console.log(data2);
          //this.tableData1.splice(xxx,xxx,xxx);
        })
        .catch(function (error) {
          console.log(error);
        });
      return data1;


      // {
      // 	"vessel_name":"PACIFIC ACE",
      // 	"sender_mail":"0",
      // 	"opendate_start":"2019-03-02",
      // 	"opendate_end":"2019-03-02",
      // 	"days":1,
      // 	"built":5,
      // 	"account":"mouses",
      // 	"dwt":0
      // }

      // var self = this;
      // this.tableData1.splice(0, this.tableData1.length);
      // var data1 = new Array();
      // var searchText1 = document.getElementById("searchText1").value;
      // console.log(searchText1);
      // //console.log(searchText.text);
      //
      //   this.axios({
      //     method: "post",
      //     url: "http://127.0.0.1:8888/users/tonnage_card_search/" ,
      //   })
      //     .then(function (response) {
      //       console.log("axios method");
      //       console.log(response);
      //       console.log(eval(response.data));
      //       // self.tableData1.splice(0, tableData1.length);
      //       var a = eval(response.data);
      //       for (var i = 0; i < a.list.length; i++) {
      //         self.tableData1.push(a.list[i].fields);
      //         //JSON.stringify(a.list[i].fields)
      //       }
      //       //console.log(data2);
      //       //this.tableData1.splice(xxx,xxx,xxx);
      //     })
      //     .catch(function (error) {
      //       console.log(error);
      //     });
      //   return data1;





    },


    searchCargo2() {
      var self = this;
      this.tableData2.splice(0, this.tableData2.length);
      var data2 = new Array();
      var searchText2 = document.getElementById("searchText2").value;
      console.log(searchText2);
      //console.log(searchText.text);
      this.axios({
        method: "get",
        url: "http://127.0.0.1:8888/users/search_cargo/" + searchText2,
      })
        .then(function (response) {
          console.log("axios method");
          console.log(response);
          console.log(eval(response.data));
          // self.tableData2.splice(0, tableData2.length);
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
          var a = eval(response.data);
          for (var i = 0; i < a.list.length; i++) {
            self.tableData2.push(a.list[i].fields);
            //JSON.stringify(a.list[i].fields)
          }
          //console.log(data2);
          //this.tableData1.splice(xxx,xxx,xxx);
        })
        .catch(function (error) {
          console.log(error);
        });
      return data2;
    },
<<<<<<< HEAD
        //   searchCargoSimple3() {
        //   var self = this;
        //   this.tableData3.splice(0, this.tableData2.length);
        //   var data3 = new Array();
        //   var searchText3 = document.getElementById("searchText3").value;
        //   console.log(searchText3);
        //   //console.log(searchText.text);
        //   this.axios({
        //     method: "get",
        //     url: "http://127.0.0.1:8888/users/search_tc/" + searchText3,
        //   })
        //     .then(function (response) {
        //       console.log("axios method");
        //       console.log(response);
        //       console.log(eval(response.data));
        //       // self.tableData3.splice(0, tableData3.length);
        //       var a = eval(response.data);
        //       for (var i = 0; i < a.list.length; i++) {
        //         self.tableData3.push(a.list[i].fields);
        //         //JSON.stringify(a.list[i].fields)
        //       }
        //       //console.log(data3);
        //       //this.tableData1.splice(xxx,xxx,xxx);
        //     })
        //     .catch(function (error) {
        //       console.log(error);
        //     });
        //   return data3;
        // },
    searchCargo3() {
      // console.log("tc_dateList");
      // console.log(this.tc_dateList);

      var self = this;
      this.tableData3.splice(0, this.tableData3.length);
      var data3 = new Array();
      // var searchText3 = document.getElementById("searchText3").value;
      if (searchText3 = document.getElementById("searchText3").value){
          var searchText3 = document.getElementById("searchText3").value;;
      }else{
        searchText3=''
      }
      console.log(searchText3);
      //console.log(searchText.text);
      var tab3_data = document.getElementById("tab3_data");

      if(this.tc_dateList[0]){
      var data_s = this.tc_dateList[0];
      var data_e = this.tc_dateList[1];
      }else{
        data_s="1990-03-02";
        data_e="3000-03-02";
      }

      // var Quantity2 = document.getElementById("Quantity2").value;
      if (document.getElementById("Quantity2").value){
        var Quantity2 = document.getElementById("Quantity2").value;
      }else{
        Quantity2=0
      }


      var conditions = {
        	"acc":searchText3,
          "sender_mail":"0",
          // "laycan_start":"2017-03-06",
          // "laycan_end":"2019-03-10",
          "laycan_start":data_s,
          "laycan_end":data_e,
          "days":1,
          "quantity":Quantity2,
          "account":""
      }


      this.axios({
        method: "post",
        url: "http://127.0.0.1:8888/users/tc_search",
        data:conditions
      })
        .then(function (response) {
          console.log("axios method");
          console.log(response);
          console.log(eval(response.data));
          // self.tableData1.splice(0, tableData1.length);
          var a = eval(response.data);
          for (var i = 0; i < a.list.length; i++) {
            self.tableData3.push(a.list[i].fields);
            //JSON.stringify(a.list[i].fields)
          }
          //console.log(data3);
          //this.tableData3.splice(xxx,xxx,xxx);
        })
        .catch(function (error) {
          console.log(error);
        });
      return data3;
    },
    handleClick(tab, event) {
      console.log(tab, event);
    },
=======

    searchCargo3() {
      var self = this;
      this.tableData3.splice(0, this.tableData2.length);
      var data3 = new Array();
      var searchText3 = document.getElementById("searchText3").value;
      console.log(searchText3);
      //console.log(searchText.text);
      this.axios({
        method: "get",
        url: "http://127.0.0.1:8888/users/search_tc/" + searchText3,
      })
        .then(function (response) {
          console.log("axios method");
          console.log(response);
          console.log(eval(response.data));
          // self.tableData3.splice(0, tableData3.length);
          var a = eval(response.data);
          for (var i = 0; i < a.list.length; i++) {
            self.tableData3.push(a.list[i].fields);
            //JSON.stringify(a.list[i].fields)
          }
          //console.log(data3);
          //this.tableData1.splice(xxx,xxx,xxx);
        })
        .catch(function (error) {
          console.log(error);
        });
      return data3;
    },


    handleClick(tab, event) {
      console.log(tab, event);
    },



>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e

  }
};
</script>


<style>
.el-header {
  background-color: #66b1ff;
<<<<<<< HEAD
  color: #060606;
=======
  color: #303133;
>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
  text-align: center;
  line-height: 60px;
}
.el-footer {
  background-color: rgba(191, 195, 214, 0.04);
<<<<<<< HEAD
  color: #bdb9ab;
  text-align: center;
  line-height: 60px;
}
.el-aside {
  background-color: #f5f7fa;
  color: rgb(189, 185, 171);
  text-align: center;
  line-height: 700px;
}
.el-main {
  background-color: rgba(214, 57, 67, 0.01);
  color: #bdb9ab;
  text-align: center;
  line-height: 20px;
}
body > .el-container {
  margin-bottom: 40px;
}
=======
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #f5f7fa;
  color: rgba(6, 5, 6, 1);
  text-align: center;
  line-height: 700px;
}

.el-main {
  background-color: rgba(214, 57, 67, 0.01);
  color: #060606;
  text-align: center;
  line-height: 20px;
}

body > .el-container {
  margin-bottom: 40px;
}

>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 60px;
}
<<<<<<< HEAD
=======

>>>>>>> d18cb0f9e000f656401513a8f0f930165fc6881e
.el-container:nth-child(7) .el-aside {
  line-height: 10px;
}
</style>
