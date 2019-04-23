
<template>
  <el-container>
    <!--<el-aside width="220px">Other msg</el-aside>-->
    <el-container>
      <el-header></el-header>
      <!--<el-header>Boat Demo</el-header>-->
      <el-main>
        <el-row :gutter="20">
          <el-col :span="17">
            <el-tabs :before-leave="clear_1" v-model="activeName2" type="card" @tab-click="handleClick" >

              <el-tab-pane  label="Tonnage Cards" name="first"   >


                <div >Tonnage offer cards</div>
                <div >
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
                      id="senderMail1"
                      type="text"
                      class="searchBox"
                      style="width:200px;height:25px;"
                    />
                  </div>
                </div>

                <div>
                  <!--Open Date 日期框的实现-->
                  <div
                    class="block"
                    style="text-align:left;display:inline ;float:left "
                  >
                    <span class="demonstration"
                      >Open Date : &nbsp;&nbsp;&nbsp;</span
                    >
                    <el-date-picker
                      unlink-panels
                      v-model="value_a_1"
                      id="tab1_data"
                      value-format="yyyy-MM-dd"
                      type="daterange"
                      range-separator="--"
                      @change="chooseTimeRange1"
                      start-placeholder="Start Date"
                      end-placeholder="End Date"
                      style="height:30px;"
                    >
                    </el-date-picker>
                  </div>

                  <!--Sent within 框的实现-->
                  <div  style="text-align:left;display:inline ">
                    &nbsp;&nbsp;Sent within : &nbsp;&nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;
                    <el-select id="sentWithin1" v-model="value_a_2" placeholder="All">
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

                  <!--Built 框的实现-->
                  <div style="text-align:left ;display:inline ;float:left">
                    Built :
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Under
                    <el-select id="built1" v-model="value_a_3" placeholder="All">
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


                  <!--Mail Account 框的实现-->
                  <div style="text-align:left;display:inline ;">
                    Mail Account
                    :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-select id="mail_Account1" v-model="value_a_4" placeholder="All">
                      <el-option
                        v-for="item in options_a_4"
                        :key="item.value_a_4"
                        :label="item.label"
                        :value="item.value_a_4"
                      >
                      </el-option>
                    </el-select>
                  </div>

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
                    DWT :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gte(>=)

                    <input
                      id="dwt1"
                      type="text"
                      class="searchBox"
                      style="width:100px;height:25px;"
                    />
                    --
                    <input
                      id="dwt2"
                      type="text"
                      class="searchBox"
                      style="width:100px;height:25px;"
                    />
                    lte(<=)
                  </div>





                  <!--Open Area 框的实现-->
                  <div
                    class="search_tonnage"
                    style="text-align:left; display:inline;"
                  >
                   Open area :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <input
                      id="searchText_open_area"
                      type="text"
                      class="searchBox"
                      style="width:200px;height:25px;"
                    />
                  </div>
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

                <!--<button-->
                  <!--@click="searchCargoSimple1"-->
                  <!--class="btn"-->
                  <!--style="text-align:center;width:150px;height:32px;font-size:15px"-->
                <!--&gt;-->
                  <!--Search_by_One-->
                <!--</button>-->

                <!--定义Complete和Incomplete按钮-->
                 <button
                  @click="incomplete1"
                  class="btn"
                  style="text-align:center;width:90px;height:32px;font-size:15px;"
                >
                  Incomplete
                </button>

                 <button
                  @click="complete1"
                  class="btn"
                  style="text-align:center;width:90px;height:32px;font-size:15px;"
                >
                  Complete
                </button>

               <!--定义Search按钮-->

                <button
                  @click="searchCargo1"
                  class="btn"
                  style="text-align:center;width:60px;height:32px;font-size:15px"
                >
                  Search
                </button>

                <button
                  onclick="window.location.reload();"
                  id = 'clear'
                  class="btn"
                  style="text-align:center;width:60px;height:32px;font-size:15px"
                >
                  Clear
                </button>



                <!-- 添加导出Excel按钮-->
                <button  @click="exportExcel"  class="btn" style="text-align:center;width:120px;height:32px;font-size:15px">Import Excel</button>

                <!-- 添加复选框按钮-->
                 <el-button  @click="displaySelection"  class="btn" style="float:right;background:rgba(238,234,214,0)">Batch Choice </el-button>





                <el-table
                  id="mytable1"
                  ref="multipleTable"
                  tooltip-effect="dark"
                  @selection-change="handleSelectionChange"

                  :data=" tableData1.slice((currentPage - 1) * pagesize,currentPage * pagesize)"
                  height="800"
                  border
                  style="width: 100%"
                  @row-click="display_mail"


                >

                  <el-table-column type="selection" width="40"  >

                  </el-table-column>

                  <el-table-column prop="flag" label="Flag" width="50">

                    <template slot-scope="scope">
                         <!--<el-button type="warning" icon="el-icon-star-off" circle></el-button>-->
                         <el-button  style="margin: 0;padding: 0;font-size: 100%;"   icon="el-icon-star-on" v-if="scope.row.flag==1  " @click=' switchChange2(scope.$index, scope.row)' ></el-button>
                         <el-button  style="margin: 0;padding: 0;font-size: 100%;"   icon="el-icon-star-off" v-else="!scope.row.flag==0" @click=' switchChange(scope.$index, scope.row)' ></el-button>
                   </template>

                   </el-table-column>

                  <el-table-column
                    prop="ID"
                    label="ID"
                    width="40"
                  >
                    <!--<template slot-scope="scope">-->
                          <!--<template  v-if="scope.row.edit">-->
                              <!--<el-input class="edit-input" size="small" v-model="scope.row.ID"></el-input>-->
                          <!--</template>-->
                          <!--<span v-else>{{ scope.row.ID }}</span>-->
                    <!--</template>-->


                  </el-table-column>


                  <el-table-column
                    prop="Vessel_name"
                    label="Vessel Name"
                    width="200"
                  >
                    <template slot-scope="scope">
                          <template  v-if="scope.row.edit">
                              <el-input class="edit-input" size="small" v-model="scope.row.Vessel_name"></el-input>
                          </template>
                          <span v-else>{{ scope.row.Vessel_name }}</span>
                    </template>


                  </el-table-column>

                  <el-table-column prop="DWT" label="DWT" width="80">
                       <template slot-scope="scope">
                          <template  v-if="scope.row.edit">
                              <el-input class="edit-input" size="small" v-model="scope.row.DWT"></el-input>
                          </template>
                          <span v-else>{{ scope.row.DWT }}</span>
                       </template>


                  </el-table-column>

                  <el-table-column id="blt1" prop="BLT" label="BLT" width="80">
                       <template slot-scope="scope">
                          <template  v-if="scope.row.edit">
                              <el-input class="edit-input" size="small" v-model="scope.row.BLT"></el-input>
                          </template>
                          <span v-else>{{ scope.row.BLT }}</span>
                       </template>

                  </el-table-column>

                  <!--<el-table-column-->
                    <!--prop="Open_area"-->
                    <!--label="Open Area"-->
                    <!--width="150"-->
                    <!--:formatter="deal_Open_area"-->
                  <!--&gt;-->
                     <!--<template slot-scope="scope">-->
                          <!--<template  v-if="scope.row.edit">-->
                              <!--<el-input class="edit-input" size="small" v-model="scope.row.Open_area"></el-input>-->
                          <!--</template>-->
                          <!--<span v-else>{{ scope.row.Open_area }}</span>-->
                       <!--</template>-->

                  <!--</el-table-column> -->

                  <el-table-column
                    prop="Open_area"
                    label="Open Area"
                    width="200"
                  >
                     <template slot-scope="scope">
                          <template  v-if="scope.row.edit">
                              <el-input class="edit-input" size="small" v-model="scope.row.Open_area"></el-input>
                          </template>
                          <span v-else v-html="deal_Open_area(scope.row,scope.column)"></span>
                       </template>

                  </el-table-column>


                  <!--实现Open_date_S和Open_date_E的合并-->
                  <!--<el-table-column-->

                    <!--label="Open Date"-->
                    <!--width="200"-->
                    <!--:formatter="deal_Open_Date"-->
                    <!--prop="Open_date"-->
                  <!--&gt;-->
                      <!--<template slot-scope="scope">-->
                          <!--<template  v-if="scope.row.edit">-->
                              <!--<el-input class="edit-input" size="small" v-model="scope.row.Open_date"></el-input>-->
                          <!--</template>-->
                          <!--<span v-else>{{ scope.row.Open_date }}</span>-->
                       <!--</template>-->
                    <!---->
                      <!--&lt;!&ndash;<template slot-scope="scope" >&ndash;&gt;-->
                        <!--&lt;!&ndash;{{scope.row.Open_date_S + '&#45;&#45;'+scope.row.Open_date_E}}&ndash;&gt;-->
                      <!--&lt;!&ndash;</template>&ndash;&gt;-->
                  <!--</el-table-column> -->
                  <el-table-column
                    id="date_1"
                    label="Open Date"
                    width="200"
                    props=[Open_date_S,Open_date_E]

                  >
                      <template slot-scope="scope">
                          <template v-if="scope.row.edit" >
                                <el-date-picker
                                  unlink-panels
                                  v-model="value13_1 "
                                  class="edit-input"
                                  value-format="yyyy-MM-dd"
                                  type="daterange"
                                  style="width: 150px"
                                  start-placeholder="Start"
                                  end-placeholder="End"
                                  @change="chooseTimeRange1_1"
                                  @blur="changeTimeValue1_1(scope.row, scope.column)"
                                  :default-time="['00:00:00', '23:59:59']" >

                                </el-date-picker>
                          </template>
                          <span  v-else v-html="deal_Open_Date(scope.row, scope.column)"></span>
                       </template>


                  </el-table-column>
                  <!--<el-table-column-->
                    <!--prop="Open_date_E"-->
                    <!--label="Open Date End"-->
                    <!--width="130"-->
                  <!--&gt;-->
                  <!--</el-table-column>-->

                  <el-table-column prop="Sent" label="Sent" width="160" :formatter="deal_Sent1" >
                  </el-table-column>



                  <!--<el-table-column prop="Sent" label="Sent"  :chargNull="chargNull" width="200">-->
                  <!--</el-table-column>-->

                  <el-table-column label="Operation" width="120">
                      <template slot-scope="scope">
                          <el-button v-if="scope.row.edit" type="success" @click="confirmEdit(scope.$index, scope.row)" size="small" icon="el-icon-circle-check-outline">Save</el-button>
                          <el-button v-else type="primary" @click='scope.row.edit=!scope.row.edit' size="small" icon="el-icon-edit">Edit</el-button>
                      </template>
                   </el-table-column>







                </el-table>



                <!--&lt;!&ndash;// 处理分页&ndash;&gt;-->
                <!--<div class="yema">-->
                <!--    <el-pagination background-->
                <!--@size-change="handleSizeChange"-->
                <!--@current-change="handleCurrentChange"-->
                <!--:current-page="currentPage"-->
                <!--:page-sizes="[5,10,15]"-->
                <!--:page-size="pagesize"-->
                <!--layout="total,jumper,prev, pager, next,sizes"-->
                <!--:total="tableData1.length" >-->
                <!--    </el-pagination>-->
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
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sender's
                    Mail : &nbsp;&nbsp;&nbsp;&nbsp;
                    <input
                      id="senderMail2"
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
                      >Laycan : &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;</span
                    >
                    <el-date-picker
                      unlink-panels
                      v-model="value_b_1"
                      id="tab2_data"
                      type="daterange"
                      value-format="yyyy-MM-dd"
                      range-separator="--"
                      start-placeholder="Start Date"
                      end-placeholder="End Date"
                      @change="chooseTimeRange2"
                      style="height:30px;"
                    >
                    </el-date-picker>
                  </div>

                  <!--Sent within 框的实现-->
                  <div style="text-align:left;display:inline ">
                    &nbsp;&nbsp;Sent within : &nbsp;&nbsp; &nbsp;&nbsp;
                    <el-select id="sentWithin2" v-model="value_b_2" placeholder="All">
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
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mail
                    Account :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-select id="mail_Account2" v-model="value_b_4" placeholder="All">
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
                    Quantity :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gte(>=)
                    <input
                      id="Quantity1"
                      type="text"
                      class="searchBox"
                      style="width:200px;height:25px;"
                    />

                  </div>


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

                <!--<button-->
                  <!--@click="searchCargoSimple2"-->
                  <!--class="btn"-->
                  <!--style="text-align:center;width:160px;height:32px;font-size:15px"-->
                <!--&gt;-->
                  <!--Search_by_One-->
                <!--</button>-->
                <!--定义Complete和Incomplete按钮-->
                 <button
                  @click="incomplete2"
                  class="btn"
                  style="text-align:center;width:90px;height:32px;font-size:15px;"
                >
                  Incomplete
                </button>

                 <button
                  @click="complete2"
                  class="btn"
                  style="text-align:center;width:90px;height:32px;font-size:15px;"
                >
                  Complete
                </button>

                <button
                  @click="searchCargo2"
                  class="btn"
                  style="text-align:center;width:60px;height:32px;font-size:15px"
                >
                  Search
                </button>

                <button
                 onclick="window.location.reload();"
                  class="btn"
                  style="text-align:center;width:60px;height:32px;font-size:15px"
                >
                  Clear
                </button>

                <!--// 添加导出Excel按钮-->
                 <button  @click="exportExcel2"  class="btn" style="text-align:center;width:120px;height:32px;font-size:15px">Import Excel</button>

                <!-- 添加复选框按钮-->
                 <el-button  @click="displaySelection2"  class="btn" style="float:right;background:rgba(238,234,214,0)">Batch Choice </el-button>



                <el-table
                  id="mytable2"

                  ref="multipleTable"
                  tooltip-effect="dark"
                  @selection-change="handleSelectionChange2"

                  :data="
                    tableData2.slice(
                      (currentPage - 1) * pagesize,
                      currentPage * pagesize
                    )
                  "
                  height="800"
                  border
                  style="width: 100%"
                  @row-click="display_mail2"

                >

                  <el-table-column type="selection" width="40"  >

                  </el-table-column>


                  <el-table-column prop="flag" label="Flag" width="50">

                    <template slot-scope="scope">
                         <!--<el-button type="warning" icon="el-icon-star-off" circle></el-button>-->
                         <el-button  icon="el-icon-star-on" style="margin: 0;padding: 0;font-size: 100%;"  v-if="scope.row.flag==1  " @click=' switchChange2_c(scope.$index, scope.row)' size="small"></el-button>
                         <el-button  icon="el-icon-star-off" style="margin: 0;padding: 0;font-size: 100%;"  v-else="!scope.row.flag==0" @click=' switchChange_c(scope.$index, scope.row)' size="small"></el-button>
                   </template>

                   </el-table-column>


                  <el-table-column
                    prop="ID"
                    label="ID"
                    width="40"
                  >
                    <!--<template slot-scope="scope">-->
                          <!--<template  v-if="scope.row.edit">-->
                              <!--<el-input class="edit-input" size="small" v-model="scope.row.ID"></el-input>-->
                          <!--</template>-->
                          <!--<span v-else>{{ scope.row.ID }}</span>-->
                    <!--</template>-->


                  </el-table-column>


                  <el-table-column
                    prop="Cargo_name"
                    label="Cargo Name"
                    width="200"

                  >
                    <template slot-scope="scope">
                      <template  v-if="scope.row.edit">
                          <el-input class="edit-input" size="small" v-model="scope.row.Cargo_name"></el-input>
                      </template>
                      <span v-else v-html="deal_Cargo_name(scope.row,scope.column)"></span>
                    </template>


                  </el-table-column>

                  <!--实现Quantity_s和Quantity_e的合并-->
                  <el-table-column
                    props=[Quantity_s,Quantity_e]
                    label="Quantity"
                    width="120"
                  >
                     <template slot-scope="scope">
                      <template  v-if="scope.row.edit">
                          <el-input width="10px" height="10px" class="edit-input"  size="small"  v-model="scope.row.Quantity_s"></el-input>
                          <el-input width="10px" height="10px" class="edit-input"  size="small" v-model="scope.row.Quantity_e"></el-input>
                      </template>
                      <span v-else v-html="deal_Quantity2(scope.row,scope.column)"></span>
                    </template>



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

                  <el-table-column
                    prop="Loading_Port"
                    label="Loading Port"
                    width="200"
                  >
                    <template slot-scope="scope">
                      <template  v-if="scope.row.edit">
                          <el-input class="edit-input" size="small" v-model="scope.row.Loading_Port"></el-input>
                      </template>
                      <span v-else v-html="deal_Loading_Port(scope.row,scope.column)"></span>
                    </template>
                  </el-table-column>

                  <el-table-column
                    prop="Discharging_Port"
                    label="Discharging Port"
                    width="200"
                  >
                    <template slot-scope="scope">
                      <template  v-if="scope.row.edit">
                          <el-input class="edit-input" size="small" v-model="scope.row.Discharging_Port"></el-input>
                      </template>
                      <span v-else v-html="deal_Discharging_Port(scope.row,scope.column)"></span>
                    </template>

                  </el-table-column>


                  <!--实现LayCan_S和LayCan_E 日期的合并-->
                  <el-table-column

                    label="LayCan"
                    width="200"
                    props=[LayCan_S,LayCan_E]
                  >
                    <template slot-scope="scope">
                      <template  v-if="scope.row.edit">
                        <el-date-picker
                            unlink-panels
                            v-model="value13_2"
                            id="tab2_data"
                            type="daterange"
                            class="edit-input"
                            value-format="yyyy-MM-dd"
                            style="width: 150px"
                            start-placeholder="Start"
                            end-placeholder="End"
                            @change="chooseTimeRange2_1"
                            @blur="changeTimeValue2_1(scope.row,scope.column)"
                            :default-time="['00:00:00', '23:59：59']"

                          >
                          </el-date-picker>

                      </template>
                      <span v-else v-html="deal_LayCan2(scope.row,scope.column)"></span>
                    </template>

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

                  <el-table-column prop="Sent" label="Sent" width="160" :formatter="deal_Sent2">
                  </el-table-column>

                  <el-table-column label="Operation" width="120">
                      <template slot-scope="scope">
                          <el-button v-if="scope.row.edit" type="success" @click="confirmEdit2(scope.$index, scope.row)" size="small" icon="el-icon-circle-check-outline">Save</el-button>
                          <el-button v-else type="primary" @click='scope.row.edit=!scope.row.edit' size="small" icon="el-icon-edit">Edit</el-button>
                      </template>
                   </el-table-column>

                </el-table>

                <!--&lt;!&ndash;// 处理分页&ndash;&gt;-->
                <!--<div class="yema">-->
                <!--    <el-pagination background-->
                <!--@size-change="handleSizeChange"-->
                <!--@current-change="handleCurrentChange"-->
                <!--:current-page="currentPage"-->
                <!--:page-sizes="[5,10,15]"-->
                <!--:page-size="pagesize"-->
                <!--layout="total,jumper,prev, pager, next,sizes"-->
                <!--:total="tableData2.length" >-->
                <!--    </el-pagination>-->
                <!--</div>-->
                <div class="yema">
                  <el-pagination
                    background
                    @size-change="handleSizeChange2"
                    @current-change="handleCurrentChange2"
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
                    Account : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
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
                      id="senderMail3"
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
                      >Laycan : &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;</span
                    >
                    <el-date-picker
                      unlink-panels
                      v-model="value_c_1"
                      id="tab3_data"
                      value-format="yyyy-MM-dd"
                      type="daterange"
                      range-separator="--"
                      start-placeholder="Start Date"
                      end-placeholder="End Date"
                      @change="chooseTimeRange3"
                      style="height:30px;"
                    >
                    </el-date-picker>
                  </div>

                  <!--Sent within 框的实现-->
                  <div style="text-align:left;display:inline ">
                    &nbsp;&nbsp;Sent within : &nbsp;&nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;
                    <el-select id="sentWithin3" v-model="value_c_2" placeholder="All">
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
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mail
                    Account :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-select id="mail_Account3" v-model="value_c_4" placeholder="All">
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
                    Quantity :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gte(>=)

                    <input
                      id="Quantity2"
                      type="text"
                      class="searchBox"
                      style="width:200px;height:25px;"
                    />
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
                <!--<button-->
                  <!--@click="searchCargoSimple3"-->
                  <!--class="btn"-->
                  <!--style="text-align:center;width:160px;height:32px;font-size:15px"-->
                <!--&gt;-->
                  <!--Search_by_One-->
                <!--</button>-->
                <!--定义Complete和Incomplete按钮-->
                 <button
                  @click="incomplete3"
                  class="btn"
                  style="text-align:center;width:90px;height:32px;font-size:15px;"
                >
                  Incomplete
                </button>

                 <button
                  @click="complete3"
                  class="btn"
                  style="text-align:center;width:90px;height:32px;font-size:15px;"
                >
                  Complete
                </button>

                <button
                  @click="searchCargo3"
                  class="btn"
                  style="text-align:center;width:60px;height:32px ;font-size:15px"
                >
                  Search
                </button>

                <button
                 onclick="window.location.reload();"
                  class="btn"
                  style="text-align:center;width:60px;height:32px;font-size:15px"
                >
                  Clear
                </button>

                <!--// 添加导出Excel按钮-->
                 <button  @click="exportExcel3"  class="btn" style="text-align:center;width:120px;height:32px;font-size:15px">Import Excel</button>

                <!-- 添加复选框按钮-->
                 <el-button  @click="displaySelection3"  class="btn" style="float:right;background:rgba(238,234,214,0)">Batch Choice </el-button>


                <el-table
                  id="mytable3"

                  ref="multipleTable"
                  tooltip-effect="dark"
                  @selection-change="handleSelectionChange3"
                  :data="
                    tableData3.slice(
                      (currentPage - 1) * pagesize,
                      currentPage * pagesize
                    )
                  "
                  height="800"
                  border
                  style="width: 100%"
                  @row-click="display_mail3"
                >
                  <el-table-column type="selection" width="40"  >

                  </el-table-column>

                  <el-table-column prop="flag" label="Flag" width="50">

                    <template slot-scope="scope">
                         <!--<el-button type="warning" icon="el-icon-star-off" circle></el-button>-->
                         <el-button  icon="el-icon-star-on" style="margin: 0;padding: 0;font-size: 100%;"  v-if="scope.row.flag==1  " @click=' switchChange2_t(scope.$index, scope.row)' size="small"></el-button>
                         <el-button  icon="el-icon-star-off" style="margin: 0;padding: 0;font-size: 100%;"  v-else="!scope.row.flag==0" @click=' switchChange_t(scope.$index, scope.row)' size="small"></el-button>
                   </template>

                   </el-table-column>
                  <el-table-column
                    prop="ID"
                    label="ID"
                    width="40"
                  >
                    <!--<template slot-scope="scope">-->
                          <!--<template  v-if="scope.row.edit">-->
                              <!--<el-input class="edit-input" size="small" v-model="scope.row.ID"></el-input>-->
                          <!--</template>-->
                          <!--<span v-else>{{ scope.row.ID }}</span>-->
                    <!--</template>-->


                  </el-table-column>


                  <el-table-column prop="Account" label="Account" width="200">
                    <template slot-scope="scope">
                          <template  v-if="scope.row.edit">
                              <el-input class="edit-input" size="small" v-model="scope.row.Account"></el-input>
                          </template>
                          <span v-else v-html="deal_Account(scope.row,scope.column)"></span>
                    </template>
                  </el-table-column>

                  <!--实现Quantity_s和Quantity_e的合并-->
                  <el-table-column
                    props=[Quantity_s,Quantity_e]
                    label="Quantity"
                    width="110"
                  >
                    <template slot-scope="scope">
                          <template  v-if="scope.row.edit">
                              <el-input width="10px" height="10px" class="edit-input" size="small" v-model="scope.row.Quantity_s"></el-input>
                              <el-input width="10px" height="10px" class="edit-input" size="small" v-model="scope.row.Quantity_e"></el-input>
                          </template>
                          <span v-else v-html="deal_Quantity3(scope.row,scope.column)"></span>
                    </template>


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
                    width="200"
                  >
                     <template slot-scope="scope">
                          <template  v-if="scope.row.edit">
                              <el-input class="edit-input" size="small" v-model="scope.row.Delivery_area"></el-input>
                          </template>
                          <span v-else v-html="deal_Delivery_area(scope.row,scope.column)"></span>
                    </template>
                  </el-table-column>
                  <el-table-column
                    prop="Redelivery_area"
                    label="Redelivery Area"
                    width="200"
                  >
                     <template slot-scope="scope">
                          <template  v-if="scope.row.edit">
                              <el-input class="edit-input" size="small" v-model="scope.row.Redelivery_area"></el-input>
                          </template>
                          <span v-else v-html="deal_Redelivery_area(scope.row,scope.column)"></span>
                    </template>

                  </el-table-column>

                  <!--实现LayCan_S和LayCan_E的合并-->
                  <el-table-column

                    label="LayCan"
                    width="200"
                    props=[LayCan_S,LayCan_E]
                  >
                    <template slot-scope="scope">
                      <template  v-if="scope.row.edit">
                        <el-date-picker
                            unlink-panels
                            v-model="value13_3"
                            id="tab3_data"
                            type="daterange"
                            class="edit-input"
                            value-format="yyyy-MM-dd"
                            style="width: 150px"
                            start-placeholder="Start"
                            end-placeholder="End"
                            @change="chooseTimeRange3_1"
                            @blur="changeTimeValue3_1(scope.row,scope.column)"
                            :default-time="['00:00:00', '23:59：59']"

                          >
                          </el-date-picker>

                      </template>
                      <span v-else v-html="deal_LayCan3(scope.row,scope.column)"></span>
                    </template>





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
                  <el-table-column  label="DUR" width="80" props=[DUR_S,DUR_E]>
                    <template slot-scope="scope">
                          <template  v-if="scope.row.edit">
                              <el-input width="10px" height="10px" class="edit-input" size="small" v-model="scope.row.DUR_S"></el-input>
                              <el-input width="10px" height="10px" class="edit-input" size="small" v-model="scope.row.DUR_E"></el-input>
                          </template>
                          <span v-else v-html="deal_DUR(scope.row,scope.column)"></span>
                    </template>


                    <!--<template slot-scope="scope">-->
                        <!--{{scope.row.DUR_S + '—'+scope.row.DUR_E}}-->
                      <!--</template>-->
                  </el-table-column>
                  <!--<el-table-column prop="DUR_E" label="DUR_E" width="70">-->
                  <!--</el-table-column>-->
                  <!--<el-table-column prop="Sent" label="Sent" width="130">-->
                  <!--</el-table-column>-->
                  <!--处理sent 中为0的数据不显示-->
                  <el-table-column prop="Sent" label="Sent" width="160" :formatter="deal_Sent3">
                  </el-table-column>

                  <el-table-column label="Operation" width="120">
                      <template slot-scope="scope">
                          <el-button v-if="scope.row.edit" type="success" @click="confirmEdit3(scope.$index, scope.row)" size="small" icon="el-icon-circle-check-outline">Save</el-button>
                          <el-button v-else type="primary" @click='scope.row.edit=!scope.row.edit' size="small" icon="el-icon-edit">Edit</el-button>
                      </template>
                   </el-table-column>





                </el-table>

                <!--&lt;!&ndash;// 处理分页&ndash;&gt;-->
                <!--<div class="yema">-->
                <!--    <el-pagination background-->
                <!--@size-change="handleSizeChange"-->
                <!--@current-change="handleCurrentChange"-->
                <!--:current-page="currentPage"-->
                <!--:page-sizes="[5,10,15]"-->
                <!--:page-size="pagesize"-->
                <!--layout="total,jumper,prev, pager, next,sizes"-->
                <!--:total="tableData3.length" >-->
                <!--    </el-pagination>-->
                <!--</div>-->
                <div class="yema">
                  <el-pagination
                    background
                    @size-change="handleSizeChange3"
                    @current-change="handleCurrentChange3"
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
                <!--<div style="overflow-x:hidden ;height:650px">-->
                <div  style="overflow:auto;height:650px;color: #060606;">
                  <!--<pre ><v-clamp  autoresize :max-lines="10" id="light1" >{{ text }}</v-clamp></pre>-->
                  <pre style="width: 100px;"  xml:lang id="light1">  {{ text }}</pre>

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


<script>
// import VClamp from 'vue-clamp'
import FileSaver from 'file-saver'
import XLSX from 'xlsx'

export default {

  data() {

    return {
      // ton 复选框方法
      multipleSelection: [],
      // cargo 复选框方法
      multipleSelection2: [],
      // tc 复选框方法
      multipleSelection3: [],


      // ton 修改table日期的方法
      value13_1: '',
      datepickertableList:[],
      // cargo 修改table日期的方法
      value13_2: '',
      datepickertable2List:[],
      // tc 修改table日期的方法
      value13_3: '',
      datepickertable3List:[],

      //定义时间选择器的初始存储
      datepickerList:[],
      cargo_dateList:[],
      tc_dateList:[],

      // 定义每次刷新时在first页面显示
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
    // var h = "202.120.32.222";

    // var tableData2 = new Array();
    this.axios({
      method: "get",
      url: "http://202.120.32.222:8888/users/cargo"
    })
      .then(function (response) {
        var a = eval(response.data);
        for (var i = 0; i < a.list.length; i++) {
          // self.tableData2.push(a.list[i].fields);
          var t=a.list[i].fields;
          t["ID"]=a.list[i].pk;
          self.tableData2.push(t);
          //JSON.stringify(a.list[i].fields)
        }
        console.log("tableData2")
        console.log(self.tableData2);
        //this.tableData2.splice(xxx,xxx,xxx);
      })
      .catch(function (error) {
        console.log(error);
      });
    // var tableData1 = new Array();
    this.axios({
      method: "get",
      url: "http://202.120.32.222:8888/users/tonnage"
    })
      .then(function (response) {
        var a = eval(response.data);
        for (var i = 0; i < a.list.length; i++) {
           var t=a.list[i].fields;
          t["ID"]=a.list[i].pk;
          self.tableData1.push(t);
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
      url: "http://202.120.32.222:8888/users/tc"
    })
      .then(function (response) {
        var a = eval(response.data);
        for (var i = 0; i < a.list.length; i++) {
          // self.tableData3.push(a.list[i].fields);
          var t=a.list[i].fields;
          t["ID"]=a.list[i].pk;
          self.tableData3.push(t);
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
          // this.value_a_2 = '';
          // var obj5 = document.getElementById('tab1_data') ;
          // this.value_a_1 = '';
          // var obj6 = document.getElementById('built1') ;
          // this.value_a_3 = '';
          // var obj7 = document.getElementById('mail_Account1') ;
          // this.value_a_4 = '';
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
           this.value_b_2 = '';
           var obj5 = document.getElementById('tab2_data') ;
           this.value_b_1 = '';
           var obj6 = document.getElementById('mail_Account2') ;
           this.value_b_4 = '';


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
           this.value_c_2 = '';
           var obj5 = document.getElementById('tab3_data') ;
           this.value_c_1 = '';
           var obj6 = document.getElementById('mail_Account3') ;
           this.value_c_4 = '';

        }

    },



    //对 tableDate3中的空数据和标识数据进行处理
    //将sent 中 0转换为空
    deal_Sent3(row, column) {
      if(row.Sent.valueOf()==0){
          return '';
      }
        // return row.Sent;
      var dateee = new Date(row.Sent.valueOf()).toJSON();
        return new Date(+new Date(dateee) + 8 * 3600 * 1000).toISOString().replace(/T/g, ' ').replace(/\.[\d]{3}Z/, '');
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
      //   // return row.LayCan_S+'--'+row.LayCan_E;
      // // 此处定义时间的英文显示
      // let date = new Date(row.LayCan_S.replace(/-/g,'/')); //Wed Jan 02 2019 00:00:00 GMT+0800 (China Standard Time)
      // let date2 = new Date(row.LayCan_E.replace(/-/g,'/')); //Wed Jan 02 2019 00:00:00 GMT+0800 (China Standard Time)
      //
      // let chinaDate = date.toDateString(); //"Tue, 01 Jan 2019 16:00:00 GMT"
      // let chinaDate2 = date2.toDateString(); //"Tue, 01 Jan 2019 16:00:00 GMT"
      // //注意：此处时间为中国时区，如果是全球项目，需要转成【协调世界时】（UTC）
      // // let globalDate = date.toUTCString(); //"Wed Jan 02 2019"
      //
      // //之后的处理是一样的
      // // let chinaDateArray = chinaDate.split(' '); //["Wed", "Jan", "02", "2019"]
      //
      // // let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]}, ${chinaDateArray[3]}`; //"Jan 02, 2019"
      // let total_date= chinaDate+"--"+chinaDate2
      //
      // return total_date
         // 此处定义时间的英文显示
      let date = new Date(row.LayCan_S.replace(/-/g,'/')); //Wed Jan 02 2019 00:00:00 GMT+0800 (China Standard Time)
      let date2 = new Date(row.LayCan_E.replace(/-/g,'/')); //Wed Jan 02 2019 00:00:00 GMT+0800 (China Standard Time)

      let chinaDate = date.toDateString(); //"Tue, 01 Jan 2019 16:00:00 GMT"
      let chinaDate2 = date2.toDateString(); //"Tue, 01 Jan 2019 16:00:00 GMT"
      //注意：此处时间为中国时区，如果是全球项目，需要转成【协调世界时】（UTC）
      // let globalDate = date.toUTCString(); //"Wed Jan 02 2019"

      //之后的处理是一样的
      // let chinaDateArray = chinaDate.split(' '); //["Wed", "Jan", "02", "2019"]
      // let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]}, ${chinaDateArray[3]}`; //"Jan 02, 2019"
      let chinaDateArray = chinaDate.split(' '); //["Wed", "Jan", "02", "2019"]
      let chinaDateArray2 = chinaDate2.split(' '); //["Wed", "Jan", "02", "2019"]

      if (chinaDateArray[3]!=chinaDateArray2[3]){
          let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]},${chinaDateArray[3]}`; //"Jan 02, 2019"
          let displayDate2 = `${chinaDateArray2[1]} ${chinaDateArray2[2]},${chinaDateArray2[3]}`; //"Jan 02, 2019"

         // let total_date= chinaDate+"--"+chinaDate2;
          let total_date= displayDate+"--"+displayDate2;
          return total_date
      }else {
        let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]}`; //"Jan 02, 2019"
        let displayDate2 = `${chinaDateArray2[1]} ${chinaDateArray2[2]}`; //"Jan 02, 2019"

        // let total_date= chinaDate+"--"+chinaDate2;
        let total_date = displayDate + "--" + displayDate2;
        return total_date
      }

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
      var dateee = new Date(row.Sent.valueOf()).toJSON();
        return new Date(+new Date(dateee) + 8 * 3600 * 1000).toISOString().replace(/T/g, ' ').replace(/\.[\d]{3}Z/, '');
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
      //   // return row.LayCan_S+'--'+row.LayCan_E;
      // // 此处定义时间的英文显示
      // let date = new Date(row.LayCan_S.replace(/-/g,'/')); //Wed Jan 02 2019 00:00:00 GMT+0800 (China Standard Time)
      // let date2 = new Date(row.LayCan_E.replace(/-/g,'/')); //Wed Jan 02 2019 00:00:00 GMT+0800 (China Standard Time)
      //
      // let chinaDate = date.toDateString(); //"Tue, 01 Jan 2019 16:00:00 GMT"
      // let chinaDate2 = date2.toDateString(); //"Tue, 01 Jan 2019 16:00:00 GMT"
      // //注意：此处时间为中国时区，如果是全球项目，需要转成【协调世界时】（UTC）
      // // let globalDate = date.toUTCString(); //"Wed Jan 02 2019"
      //
      // //之后的处理是一样的
      // // let chinaDateArray = chinaDate.split(' '); //["Wed", "Jan", "02", "2019"]
      //
      // // let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]}, ${chinaDateArray[3]}`; //"Jan 02, 2019"
      // let total_date= chinaDate+"--"+chinaDate2
      //
      // return total_date
         // 此处定义时间的英文显示
      let date = new Date(row.LayCan_S.replace(/-/g,'/')); //Wed Jan 02 2019 00:00:00 GMT+0800 (China Standard Time)
      let date2 = new Date(row.LayCan_E.replace(/-/g,'/')); //Wed Jan 02 2019 00:00:00 GMT+0800 (China Standard Time)

      let chinaDate = date.toDateString(); //"Tue, 01 Jan 2019 16:00:00 GMT"
      let chinaDate2 = date2.toDateString(); //"Tue, 01 Jan 2019 16:00:00 GMT"
      //注意：此处时间为中国时区，如果是全球项目，需要转成【协调世界时】（UTC）
      // let globalDate = date.toUTCString(); //"Wed Jan 02 2019"

      //之后的处理是一样的
      // let chinaDateArray = chinaDate.split(' '); //["Wed", "Jan", "02", "2019"]
      // let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]}, ${chinaDateArray[3]}`; //"Jan 02, 2019"
      let chinaDateArray = chinaDate.split(' '); //["Wed", "Jan", "02", "2019"]
      let chinaDateArray2 = chinaDate2.split(' '); //["Wed", "Jan", "02", "2019"]

      if (chinaDateArray[3]!=chinaDateArray2[3]){
          let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]},${chinaDateArray[3]}`; //"Jan 02, 2019"
          let displayDate2 = `${chinaDateArray2[1]} ${chinaDateArray2[2]},${chinaDateArray2[3]}`; //"Jan 02, 2019"

         // let total_date= chinaDate+"--"+chinaDate2;
          let total_date= displayDate+"--"+displayDate2;
          return total_date
      }else {
        let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]}`; //"Jan 02, 2019"
        let displayDate2 = `${chinaDateArray2[1]} ${chinaDateArray2[2]}`; //"Jan 02, 2019"

        // let total_date= chinaDate+"--"+chinaDate2;
        let total_date = displayDate + "--" + displayDate2;
        return total_date
      }

    },

    // 对 tableDate1中的空数据和标识数据进行处理
    //将Sent 中 标识0转换为空
    deal_Sent1(row, column) {
      if(row.Sent.valueOf()==0){
          return '';
      }
      var dateee = new Date(row.Sent.valueOf()).toJSON();
        return new Date(+new Date(dateee) + 8 * 3600 * 1000).toISOString().replace(/T/g, ' ').replace(/\.[\d]{3}Z/, '');
    },
    //将Open_area 中 标识sting转换为空
    deal_Open_area(row, column) {
      if(row.Open_area.valueOf()=='no open area match'){
          return '';
      }
        return row.Open_area;
    },
    //将Open_Date 中 标识sting转换为空
    // deal_Open_Date(row, column) {
    //   if(row.Open_date_S+'--'+row.Open_date_E.valueOf()=='1900-01-01--1900-01-01'){
    //       return '';
    //   }
    //     // return row.Open_date_S+'--'+row.Open_date_E;
    //
    //   // 此处定义时间的英文显示
    //   let date = new Date(row.Open_date_S.replace(/-/g,'/')); //Wed Jan 02 2019 00:00:00 GMT+0800 (China Standard Time)
    //   let date2 = new Date(row.Open_date_E.replace(/-/g,'/')); //Wed Jan 02 2019 00:00:00 GMT+0800 (China Standard Time)
    //
    //   let chinaDate = date.toDateString(); //"Tue, 01 Jan 2019 16:00:00 GMT"
    //   let chinaDate2 = date2.toDateString(); //"Tue, 01 Jan 2019 16:00:00 GMT"
    //   //注意：此处时间为中国时区，如果是全球项目，需要转成【协调世界时】（UTC）
    //   // let globalDate = date.toUTCString(); //"Wed Jan 02 2019"
    //
    //   //之后的处理是一样的
    //   // let chinaDateArray = chinaDate.split(' '); //["Wed", "Jan", "02", "2019"]
    //   // let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]}, ${chinaDateArray[3]}`; //"Jan 02, 2019"
    //   let chinaDateArray = chinaDate.split(' '); //["Wed", "Jan", "02", "2019"]
    //   let chinaDateArray2 = chinaDate2.split(' '); //["Wed", "Jan", "02", "2019"]
    //
    //   if (chinaDateArray[3]!=chinaDateArray2[3]){
    //       let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]},${chinaDateArray[3]}`; //"Jan 02, 2019"
    //       let displayDate2 = `${chinaDateArray2[1]} ${chinaDateArray2[2]},${chinaDateArray2[3]}`; //"Jan 02, 2019"
    //
    //      // let total_date= chinaDate+"--"+chinaDate2;
    //       let total_date= displayDate+"--"+displayDate2;
    //       return total_date
    //   }else {
    //       let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]}`; //"Jan 02, 2019"
    //       let displayDate2 = `${chinaDateArray2[1]} ${chinaDateArray2[2]}`; //"Jan 02, 2019"
    //
    //      // let total_date= chinaDate+"--"+chinaDate2;
    //       let total_date= displayDate+"--"+displayDate2;
    //       return total_date
    //   }
    //
    // },
    deal_Open_Date(row, column) {
      if(row.Open_date_S+'--'+row.Open_date_E.valueOf()=='1900-01-01--1900-01-01'){
          return '';
      }
        // return row.Open_date_S+'--'+row.Open_date_E;

      // 此处定义时间的英文显示
      let date = new Date(row.Open_date_S.replace(/-/g,'/')); //Wed Jan 02 2019 00:00:00 GMT+0800 (China Standard Time)
      let date2 = new Date(row.Open_date_E.replace(/-/g,'/')); //Wed Jan 02 2019 00:00:00 GMT+0800 (China Standard Time)

      let chinaDate = date.toDateString(); //"Tue, 01 Jan 2019 16:00:00 GMT"
      let chinaDate2 = date2.toDateString(); //"Tue, 01 Jan 2019 16:00:00 GMT"
      //注意：此处时间为中国时区，如果是全球项目，需要转成【协调世界时】（UTC）
      // let globalDate = date.toUTCString(); //"Wed Jan 02 2019"

      //之后的处理是一样的
      // let chinaDateArray = chinaDate.split(' '); //["Wed", "Jan", "02", "2019"]
      // let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]}, ${chinaDateArray[3]}`; //"Jan 02, 2019"
      let chinaDateArray = chinaDate.split(' '); //["Wed", "Jan", "02", "2019"]
      let chinaDateArray2 = chinaDate2.split(' '); //["Wed", "Jan", "02", "2019"]

      if (chinaDateArray[3]!=chinaDateArray2[3]){
          let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]},${chinaDateArray[3]}`; //"Jan 02, 2019"
          let displayDate2 = `${chinaDateArray2[1]} ${chinaDateArray2[2]},${chinaDateArray2[3]}`; //"Jan 02, 2019"

         // let total_date= chinaDate+"--"+chinaDate2;
          let total_date= displayDate+"--"+displayDate2;
          return total_date
      }else {
          let displayDate = `${chinaDateArray[1]} ${chinaDateArray[2]}`; //"Jan 02, 2019"
          let displayDate2 = `${chinaDateArray2[1]} ${chinaDateArray2[2]}`; //"Jan 02, 2019"

         // let total_date= chinaDate+"--"+chinaDate2;
          let total_date= displayDate+"--"+displayDate2;
          return total_date
      }

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

    // tonnage talbe行 点击方法 和 高亮显示方法
    display_mail(row) {
      // console.log("display mail method");
      // console.log(row['mail_text']);
      this.text = row['mail_text'];

      // console.log(this.text.valueOf());
      // console.log(row.Vessel_name.valueOf());

      // 高亮显示code
      var content = row.Vessel_name.valueOf();
      var content1 = row.BLT.valueOf();
      var content2 = row.Open_area.valueOf().slice(0,8);
      var content3 = row.DWT.valueOf().toString().slice(0,2)+",";


      var reg = new RegExp("(" + content + ")", "g");
      var reg1 = new RegExp("(" + content1 + ")", "g");
      var reg2 = new RegExp("(" + content2 + ")", "g");
      var reg3 = new RegExp("(" + content3 + ")", "g");

      var str = this.text;

      var newstr = str.replace(reg, "<span style=\"color:#2594ff\">$1</span>").replace(reg1, "<span style=\"color:#2594ff\">$1</span>")
        .replace(reg2, "<span style=\"color:#2594ff\">$1</span>").replace(reg3, "<span style=\"color:#2594ff\">$1</span>");

      // document.write(newstr + "<br />")


		  document.getElementById('light1').innerHTML=newstr;




    },

     // cargo talbe行 点击方法 和 高亮显示方法
    display_mail2(row) {
      // console.log("display mail method");
      // console.log(row['mail_text']);
      this.text = row['mail_text'];

      // console.log(this.text.valueOf());
      // console.log(row.Vessel_name.valueOf());

      // 高亮显示code
      var content = row.Cargo_name.valueOf().toUpperCase() ;
      var content1 = row.Loading_Port.valueOf().slice(0,4);
      var content2 = row.Discharging_Port.valueOf().slice(0,3);
      var content3 = row.Quantity_s.valueOf().toString().slice(0,2);


      var reg = new RegExp("(" + content + ")", "g");
      var reg1 = new RegExp("(" + content1 + ")", "g");
      var reg2 = new RegExp("(" + content2 + ")", "g");
      var reg3 = new RegExp("(" + content3 + ")", "g");

      var str = this.text;

      var newstr = str.replace(reg, "<span style=\"color:#2594ff\">$1</span>")
        .replace(reg1, "<span style=\"color:#2594ff\">$1</span>")
       .replace(reg2, "<span style=\"color:#2594ff\">$1</span>")
        .replace(reg3, "<span style=\"color:#2594ff\">$1</span>");

      // document.write(newstr + "<br />")


		  document.getElementById('light1').innerHTML=newstr;




    },
    // tc talbe行 点击方法 和 高亮显示方法
    display_mail3(row) {
      // console.log("display mail method");
      // console.log(row['mail_text']);
      this.text = row['mail_text'];

      // console.log(this.text.valueOf());
      // console.log(row.Vessel_name.valueOf());

      // 高亮显示code
      var content = row.Account.valueOf();
      var content1 = row.Delivery_area.valueOf().slice(0,4);
      var content2 = row.Redelivery_area.valueOf().slice(0,4);
      var content3 = row.DUR_S.valueOf().toString();
      var content4 = row.Quantity_s.valueOf().toString();


      var reg = new RegExp("(" + content + ")", "g");
      var reg1 = new RegExp("(" + content1 + ")", "g");
      var reg2 = new RegExp("(" + content2 + ")", "g");
      var reg3 = new RegExp("(" + content3 + ")", "g");
      var reg4 = new RegExp("(" + content3 + ")", "g");

      var str = this.text;

      var newstr = str.replace(reg, "<span style=\"color:#2594ff\">$1</span>")
       .replace(reg1, "<span style=\"color:#2594ff\">$1</span>")
        .replace(reg2, "<span style=\"color:#2594ff\">$1</span>")
      .replace(reg3, "<span style=\"color:#2594ff\">$1</span>").replace(reg4, "<span style=\"color:#2594ff\">$1</span>");

      // document.write(newstr + "<br />")


		  document.getElementById('light1').innerHTML=newstr;




    },




    ///处理分页 初始页currentPage、初始每页数据数pagesize和数据tableDate1,tableDate2,tableDate3
    handleSizeChange: function (size) {
      this.pagesize = size;
    },
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage;
    },

    handleSizeChange2: function (size) {
      this.pagesize = size;
    },
    handleCurrentChange2: function (currentPage) {
      this.currentPage = currentPage;
    },

    handleSizeChange3: function (size) {
      this.pagesize = size;
    },
    handleCurrentChange3: function (currentPage) {
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
    //           url: "http://202.120.32.222:8888/users/search_tonnage/" + searchText1,
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

      if (searchText_open_area = document.getElementById("searchText_open_area").value){
          var searchText_open_area = document.getElementById("searchText_open_area").value;
      }else{
        searchText_open_area=''
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
      if (document.getElementById("dwt2").value){
        var dwt2 = document.getElementById("dwt2").value;
      }else{
        dwt2=10000000
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
        "open_area":searchText_open_area,
        "dwt": dwt1,
        "dwt2": dwt2

      }


      this.axios({
        method: "post",
        url: "http://202.120.32.222:8888/users/tonnage_search",
        data:conditions
      })
        .then(function (response) {

          console.log("axios method");
          console.log(response);
          console.log(eval(response.data));
          // self.tableData1.splice(0, tableData1.length);
          var a = eval(response.data);
          for (var i = 0; i < a.list.length; i++) {
             var t=a.list[i].fields;
                  t["ID"]=a.list[i].pk;
                  self.tableData1.push(t);
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

    // 显示全部缺失信息方法
    incomplete1() {
         var self = this;
          this.tableData1.splice(0, this.tableData1.length);
          var data1 = new Array();

            this.axios({
              method: "get",
              url: "http://202.120.32.222:8888/users/ton_incomplete" ,
            })
              .then(function (response) {

                console.log("axios method");
                console.log(response);
                console.log(eval(response.data));
                // self.tableData1.splice(0, tableData1.length);
                var a = eval(response.data);
                for (var i = 0; i < a.list.length; i++) {
                  var t=a.list[i].fields;
                  t["ID"]=a.list[i].pk;
                  self.tableData1.push(t);
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
    // 显示全部完整信息方法
    complete1() {
         var self = this;
          this.tableData1.splice(0, this.tableData1.length);
          var data1 = new Array();

            this.axios({
              method: "get",
              url: "http://202.120.32.222:8888/users/ton_complete" ,
            })
              .then(function (response) {

                console.log("axios method");
                console.log(response);
                console.log(eval(response.data));
                // self.tableData1.splice(0, tableData1.length);
                var a = eval(response.data);
                for (var i = 0; i < a.list.length; i++) {

                  var t=a.list[i].fields;
                  t["ID"]=a.list[i].pk;
                  self.tableData1.push(t);

                  //JSON.stringify(a.list[i].fields)
                }
                console.log(data2);
                //this.tableData1.splice(xxx,xxx,xxx);
              }

              )
              .catch(function (error) {
                console.log(error);
              });
            return data1;

    },
    // 显示全部缺失信息方法
    incomplete2() {
         var self = this;
          this.tableData2.splice(0, this.tableData2.length);
          var data2 = new Array();

            this.axios({
              method: "get",
              url: "http://202.120.32.222:8888/users/car_incomplete" ,
            })
              .then(function (response) {

                console.log("axios method");
                console.log(response);
                console.log(eval(response.data));
                // self.tableData1.splice(0, tableData2.length);
                var a = eval(response.data);
                for (var i = 0; i < a.list.length; i++) {
                  // self.tableData2.push(a.list[i].fields);
                  var t=a.list[i].fields;
                  t["ID"]=a.list[i].pk;
                  self.tableData2.push(t);
                  //JSON.stringify(a.list[i].fields)
                }
                //console.log(data2);
                //this.tableData1.splice(xxx,xxx,xxx);
              }

              )
              .catch(function (error) {
                console.log(error);
              });
            return data2;

    },
    // 显示全部完整信息方法
    complete2() {
          var self = this;
          this.tableData2.splice(0, this.tableData2.length);
          var data2 = new Array();

            this.axios({
              method: "get",
              url: "http://202.120.32.222:8888/users/car_complete" ,
            })
              .then(function (response) {

                console.log("axios method");
                console.log(response);
                console.log(eval(response.data));
                // self.tableData1.splice(0, tableData1.length);
                var a = eval(response.data);
                for (var i = 0; i < a.list.length; i++) {
                  // self.tableData2.push(a.list[i].fields);
                  var t=a.list[i].fields;
                  t["ID"]=a.list[i].pk;
                  self.tableData2.push(t);
                  //JSON.stringify(a.list[i].fields)
                }
                //console.log(data2);
                //this.tableData2.splice(xxx,xxx,xxx);
              }

              )
              .catch(function (error) {
                console.log(error);
              });
            return data2;

    },
    // 显示全部缺失信息方法
    incomplete3() {
         var self = this;
          this.tableData3.splice(0, this.tableData3.length);
          var data3 = new Array();

            this.axios({
              method: "get",
              url: "http://202.120.32.222:8888/users/tc_incomplete" ,
            })
              .then(function (response) {

                console.log("axios method");
                console.log(response);
                console.log(eval(response.data));
                // self.tableData3.splice(0, tableData3.length);
                var a = eval(response.data);
                for (var i = 0; i < a.list.length; i++) {
                  // self.tableData3.push(a.list[i].fields);
                  var t=a.list[i].fields;
                  t["ID"]=a.list[i].pk;
                  self.tableData3.push(t);
                  //JSON.stringify(a.list[i].fields)
                }
                //console.log(data3);
                //this.tableData1.splice(xxx,xxx,xxx);
              }

              )
              .catch(function (error) {
                console.log(error);
              });
            return data3;

    },
    // 显示全部完整信息方法
    complete3() {
          var self = this;
          this.tableData3.splice(0, this.tableData3.length);
          var data3 = new Array();

            this.axios({
              method: "get",
              url: "http://202.120.32.222:8888/users/tc_complete" ,
            })
              .then(function (response) {

                console.log("axios method");
                console.log(response);
                console.log(eval(response.data));
                // self.tableData3.splice(0, tableData3.length);
                var a = eval(response.data);
                for (var i = 0; i < a.list.length; i++) {
                  // self.tableData3.push(a.list[i].fields);
                  var t=a.list[i].fields;
                  t["ID"]=a.list[i].pk;
                  self.tableData3.push(t);
                  //JSON.stringify(a.list[i].fields)
                }
                //console.log(data3);
                //this.tableData3.splice(xxx,xxx,xxx);
              }

              )
              .catch(function (error) {
                console.log(error);
              });
            return data3;

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
     //        url: "http://202.120.32.222:8888/users/search_cargo/" + searchText2,
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

      }

      this.axios({
        method: "post",
        url: "http://202.120.32.222:8888/users/cargo_search",
        data:conditions
      })
        .then(function (response) {
          console.log("axios method");
          console.log(response);
          console.log(eval(response.data));
          // self.tableData1.splice(0, tableData2.length);
          var a = eval(response.data);
          for (var i = 0; i < a.list.length; i++) {
            // self.tableData2.push(a.list[i].fields);
                  var t=a.list[i].fields;
                  t["ID"]=a.list[i].pk;
                  self.tableData2.push(t);
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
        //   searchCargoSimple3() {
        //   var self = this;
        //   this.tableData3.splice(0, this.tableData2.length);
        //   var data3 = new Array();
        //   var searchText3 = document.getElementById("searchText3").value;
        //   console.log(searchText3);
        //   //console.log(searchText.text);
        //   this.axios({
        //     method: "get",
        //     url: "http://202.120.32.222:8888/users/search_tc/" + searchText3,
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
        url: "http://202.120.32.222:8888/users/tc_search",
        data:conditions
      })
        .then(function (response) {
          console.log("axios method");
          console.log(response);
          console.log(eval(response.data));
          // self.tableData1.splice(0, tableData1.length);
          var a = eval(response.data);
          for (var i = 0; i < a.list.length; i++) {
            // self.tableData3.push(a.list[i].fields);
            var t=a.list[i].fields;
            t["ID"]=a.list[i].pk;
            self.tableData3.push(t);
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

    // ton导出Excel方法
    exportExcel() {
      // 设置当前日期
      let date = new Date();

      // let local_time = time.toLocaleString();
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      month = month < 10 ? '0' + month : month;
      let day = date.getDate();
      day = day < 10 ? ('0' + day) : day;
      let hour = date.getHours();
      hour=hour < 10 ? ('0' + hour) : hour;
      let minute = date.getMinutes();
      minute = minute < 10 ? ('0' + minute) : minute;
      let second=date.getSeconds();
      second=second < 10 ? ('0' + second) : second;

      let name = year + '-' + month + '-' + day+' '+hour+':'+minute+':'+second;

      // console.log(name)
      /* generate workbook object from table */
      //  通过 id #mytable1 指明导出的是哪一个表格
      var wb = XLSX.utils.table_to_book(document.querySelector("#mytable1"));

      /* get binary string as output */
      var wbout = XLSX.write(wb, {
        bookType: "xlsx",
        bookSST: true,
        type: "array",


      });
      try {
        //  name+'.xlsx'表示导出的excel表格名字
        FileSaver.saveAs(
          new Blob([wbout], { type: "application/octet-stream" }),
          name + ".xlsx"
        );
      } catch (e) {
        if (typeof console !== "undefined") console.log(e, wbout);
      }
      return wbout;
    },
    // cargo导出Excel方法
    exportExcel2() {
      // 设置当前日期
      let date = new Date();

      // let local_time = time.toLocaleString();
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      month = month < 10 ? '0' + month : month;
      let day = date.getDate();
      day = day < 10 ? ('0' + day) : day;
      let hour = date.getHours();
      hour=hour < 10 ? ('0' + hour) : hour;
      let minute = date.getMinutes();
      minute = minute < 10 ? ('0' + minute) : minute;
      let second=date.getSeconds();
      second=second < 10 ? ('0' + second) : second;

      let name = year + '-' + month + '-' + day+' '+hour+':'+minute+':'+second;

      // console.log(name)
      /* generate workbook object from table */
      //  通过 id #mytable1 指明导出的是哪一个表格
      var wb = XLSX.utils.table_to_book(document.querySelector("#mytable2"));
      /* get binary string as output */
      var wbout = XLSX.write(wb, {
        bookType: "xlsx",
        bookSST: true,
        type: "array"
      });
      try {
        //  name+'.xlsx'表示导出的excel表格名字
        FileSaver.saveAs(
          new Blob([wbout], { type: "application/octet-stream" }),
          name + ".xlsx"
        );
      } catch (e) {
        if (typeof console !== "undefined") console.log(e, wbout);
      }
      return wbout;
    },
    // tc导出Excel方法
    exportExcel3() {
      // 设置当前日期
      let date = new Date();

      // let local_time = time.toLocaleString();
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      month = month < 10 ? '0' + month : month;
      let day = date.getDate();
      day = day < 10 ? ('0' + day) : day;
      let hour = date.getHours();
      hour=hour < 10 ? ('0' + hour) : hour;
      let minute = date.getMinutes();
      minute = minute < 10 ? ('0' + minute) : minute;
      let second=date.getSeconds();
      second=second < 10 ? ('0' + second) : second;

      let name = year + '-' + month + '-' + day+' '+hour+':'+minute+':'+second;

      // console.log(name)
      /* generate workbook object from table */
      //  通过 id #mytable1 指明导出的是哪一个表格
      var wb = XLSX.utils.table_to_book(document.querySelector("#mytable3"));
      /* get binary string as output */
      var wbout = XLSX.write(wb, {
        bookType: "xlsx",
        bookSST: true,
        type: "array"
      });
      try {
        //  name+'.xlsx'表示导出的excel表格名字
        FileSaver.saveAs(
          new Blob([wbout], { type: "application/octet-stream" }),
          name + ".xlsx"
        );
      } catch (e) {
        if (typeof console !== "undefined") console.log(e, wbout);
      }
      return wbout;
    },

    // 添加ton编辑保存功能的方法
    confirmEdit(index,row){
    row.edit = false;
    this.$message({
        message: 'The message has been modified successfully',
        type: 'success'
        });

     var data1 = new Array();
      // console.log("编辑后修改的数据");
      //
      // console.log(row.valueOf())
      // console.log(row.valueOf().ID)
      // console.log(row.valueOf().BLT)
      // console.log(row.valueOf().DWT)
      // console.log(row.valueOf().Open_area)
      // console.log(row.valueOf().Vessel_name)
      var conditions = {
        "Vessel_name":row.valueOf().Vessel_name,
        "DWT":row.valueOf().DWT,
        "BLT":row.valueOf().BLT,
        "Sent":row.valueOf().Sent,
        "ID":row.valueOf().ID,
        "Open_date_S":row.valueOf().Open_date_S,
        "Open_date_E":row.valueOf().Open_date_E,
        "mail_text":row.valueOf().mail_text,
        "Open_area":row.valueOf().Open_area
      };

      this.axios({
        method: "put",
        url: "http://202.120.32.222:8888/users/tonnage_update",
        data:conditions
      })
        .then(function (response) {

            console.log(response);

          }

        )
        .catch(function (error) {
          console.log(error);
        });
       return data1;


    },
    // 添加cargo编辑保存功能的方法
    confirmEdit2(index,row){
    row.edit = false;
    this.$message({
        message: 'The message has been modified successfully',
        type: 'success'
        });
    var data2 = new Array();

      // console.log("编辑后修改的数据");
      //
      // console.log(row.valueOf())
      // console.log(row.valueOf().ID)
      // console.log(row.valueOf().BLT)
      // console.log(row.valueOf().DWT)
      // console.log(row.valueOf().Open_area)
      // console.log(row.valueOf().Vessel_name)
      var conditions = {
        	"Cargo_name":row.valueOf().Cargo_name,
          "Loading_Port":row.valueOf().Loading_Port,
          "Discharging_Port":row.valueOf().Discharging_Port,
          "Sent":row.valueOf().Sent,
          "ID":row.valueOf().ID,
          "LayCan_S":row.valueOf().LayCan_S,
          "LayCan_E":row.valueOf().LayCan_E,
          "Quantity_s":row.valueOf().Quantity_s,
          "Quantity_e":row.valueOf().Quantity_e,
           "mail_text":row.valueOf().mail_text


      };

      this.axios({
        method: "put",
        url: "http://202.120.32.222:8888/users/cargo_update",
        data:conditions
      })
        .then(function (response) {

          // console.log("axios method");
          // console.log(response);
          // console.log(eval(response.data));
          // // self.tableData1.splice(0, tableData1.length);
          // var a = eval(response.data);
          // for (var i = 0; i < a.list.length; i++) {
          //    var t=a.list[i].fields;
          //         t["ID"]=a.list[i].pk;
          //         self.tableData1.push(t);
          //   //JSON.stringify(a.list[i].fields)
          // }
          //  alert("The message has been update successfully")
          //console.log(data2);
          //this.tableData1.splice(xxx,xxx,xxx);
        }

        )
        .catch(function (error) {
          console.log(error);
        });
      return data2;





    },
    // 添加tc编辑保存功能的方法
    confirmEdit3(index,row){
    row.edit = false;
    this.$message({
        message: 'The message has been modified successfully',
        type: 'success'
        });
    var data3 = new Array();

      // console.log("编辑后修改的数据");
      //
      // console.log(row.valueOf())
      // console.log(row.valueOf().ID)
      // console.log(row.valueOf().BLT)
      // console.log(row.valueOf().DWT)
      // console.log(row.valueOf().Open_area)
      // console.log(row.valueOf().Vessel_name)
      var conditions = {

          "Account":row.valueOf().Account,
          "Delivery_area":row.valueOf().Delivery_area,
          "Redelivery_area":row.valueOf().Redelivery_area,
          "Sent":row.valueOf().Sent,
          "ID":row.valueOf().ID,
          "LayCan_E":row.valueOf().LayCan_E,
          "LayCan_S":row.valueOf().LayCan_S,
          "mail_text":row.valueOf().mail_text,
          "Quantity_s":row.valueOf().Quantity_s,
          "Quantity_e":row.valueOf().Quantity_e,
          "DUR_S":row.valueOf().DUR_S,
          "DUR_E":row.valueOf().DUR_E


      };

      this.axios({
        method: "put",
        url: "http://202.120.32.222:8888/users/tc_update",
        data:conditions
      })
        .then(function (response) {

          // console.log("axios method");
          // console.log(response);
          // console.log(eval(response.data));
          // // self.tableData1.splice(0, tableData1.length);
          // var a = eval(response.data);
          // for (var i = 0; i < a.list.length; i++) {
          //    var t=a.list[i].fields;
          //         t["ID"]=a.list[i].pk;
          //         self.tableData1.push(t);
          //   //JSON.stringify(a.list[i].fields)
          // }
          //  alert("The message has been update successfully")
          //console.log(data2);
          //this.tableData1.splice(xxx,xxx,xxx);
        }

        )
        .catch(function (error) {
          console.log(error);
        });
      return data3;





    },

    // ton 增加星标的方法
    switchChange(index,row){
      console.log("第二次点击");
      row.flag = !row.flag ;
      var data={
          "ID":row.valueOf().ID,
          "value":1
      };
      this.axios({
        method: "put",
        url: "http://202.120.32.222:8888/users/ton_flag",
        data:data
      })
        .then(function (response) {
          // res=eval(response);
          // console.log(res);
          // alert(res);

          // icon="el-icon-star-on"
          // document.getElementById('light1').innerHTML=icon;
            if(row.valueOf().flag){
             console.log("ok");
            // alert("ok")
          }


        }
        )
        .catch(function (error) {
          console.log(error);
        });


      },
    switchChange2(index,row){
      console.log("第一次点击");
      row.flag = !row.flag ;
      var data={
          "ID":row.valueOf().ID,
          "value":0
      };
      this.axios({
        method: "put",
        url: "http://202.120.32.222:8888/users/ton_flag",
        data:data
      })
        .then(function (response) {
          // res=eval(response);
          // console.log(res);
          // alert(res);

        }
        )
        .catch(function (error) {
          console.log(error);
        });

      },

    // cargo 增加星标的方法
    switchChange_c(index,row){
      console.log("第二次点击");
      row.flag = !row.flag ;
      var data={
          "ID":row.valueOf().ID,
          "value":1
      };
      this.axios({
        method: "put",
        url: "http://202.120.32.222:8888/users/cargo_flag",
        data:data
      })
        .then(function (response) {
          // res=eval(response);
          // console.log(res);
          // alert(res);

          // icon="el-icon-star-on"
          // document.getElementById('light1').innerHTML=icon;
            if(row.valueOf().flag){
             console.log("ok");
            // alert("ok")
          }


        }
        )
        .catch(function (error) {
          console.log(error);
        });


      },
    switchChange2_c(index,row){
      console.log("第一次点击");
      row.flag = !row.flag ;
      var data={
          "ID":row.valueOf().ID,
          "value":0
      };
      this.axios({
        method: "put",
        url: "http://202.120.32.222:8888/users/cargo_flag",
        data:data
      })
        .then(function (response) {
          // res=eval(response);
          // console.log(res);
          // alert(res);

        }
        )
        .catch(function (error) {
          console.log(error);
        });

      },

     // tc 增加星标的方法
    switchChange_t(index,row){
      console.log("第二次点击");
      row.flag = !row.flag ;
      var data={
          "ID":row.valueOf().ID,
          "value":1
      };
      this.axios({
        method: "put",
        url: "http://202.120.32.222:8888/users/tc_flag",
        data:data
      })
        .then(function (response) {
          // res=eval(response);
          // console.log(res);
          // alert(res);

          // icon="el-icon-star-on"
          // document.getElementById('light1').innerHTML=icon;
            if(row.valueOf().flag){
             console.log("ok");
            // alert("ok")
          }


        }
        )
        .catch(function (error) {
          console.log(error);
        });


      },
    switchChange2_t(index,row){
      console.log("第一次点击");
      row.flag = !row.flag ;
      var data={
          "ID":row.valueOf().ID,
          "value":0
      };
      this.axios({
        method: "put",
        url: "http://202.120.32.222:8888/users/tc_flag",
        data:data
      })
        .then(function (response) {
          // res=eval(response);
          // console.log(res);
          // alert(res);

        }
        )
        .catch(function (error) {
          console.log(error);
        });

      },


    // ton 修改table日期的方法
    chooseTimeRange1_1(t) {

      this.datepickertableList.splice(0,this.datepickertableList.length);
       for(var i=0;i<t.length;i++){
         this.datepickertableList.push(t[i]);
       }
      console.log("哈哈哈")
      console.log(this.datepickertableList);//结果为一个数组，如：["2018-08-04", "2018-08-06"]


    },
    changeTimeValue1_1(row, column){
      console.log("嘻嘻嘻")
      console.log(this.datepickertableList);
      console.log(row.valueOf().ID)
      var data_s = this.datepickertableList[0];
      var data_e = this.datepickertableList[1];

      console.log(data_s)
      console.log(data_e)

      var conditions = {
        "ID":row.valueOf().ID,
        "opendate_start": data_s,
        "opendate_end": data_e
      }

      console.log(conditions)

      this.axios({
        method: "put",
        url: "http://202.120.32.222:8888/users/ton_date",
        data:conditions
      })
        .then(function (response) {
          window.location.reload(true);


        }

        )
        .catch(function (error) {
          console.log(error);
        });


      },


    // cargo 修改table日期的方法
    chooseTimeRange2_1(t) {

      this.datepickertable2List.splice(0,this.datepickertable2List.length);
       for(var i=0;i<t.length;i++){
         this.datepickertable2List.push(t[i]);
       }
      console.log("哈哈哈")
      console.log(this.datepickertable2List);//结果为一个数组，如：["2018-08-04", "2018-08-06"]


    },
    changeTimeValue2_1(row, column){
      console.log("嘻嘻嘻")
      console.log(this.datepickertable2List);
      console.log(row.valueOf().ID)
      var data_s = this.datepickertable2List[0];
      var data_e = this.datepickertable2List[1];

      console.log(data_s)
      console.log(data_e)

      var conditions2 = {
        "ID":row.valueOf().ID,
        "laycan_start": data_s,
        "laycan_end": data_e
      }

      console.log(conditions2)

      this.axios({
        method: "put",
        url: "http://202.120.32.222:8888/users/cargo_date",
        data:conditions2
      })
        .then(function (response) {
          window.location.reload(true);


        }

        )
        .catch(function (error) {
          console.log(error);
        });


      },


    // tc修改table日期的方法
    chooseTimeRange3_1(t) {

      this.datepickertable3List.splice(0,this.datepickertable3List.length);
       for(var i=0;i<t.length;i++){
         this.datepickertable3List.push(t[i]);
       }
      console.log("哈哈哈")
      console.log(this.datepickertable3List);//结果为一个数组，如：["2018-08-04", "2018-08-06"]


    },
    changeTimeValue3_1(row, column){
      console.log("嘻嘻嘻")
      console.log(this.datepickertable3List);
      console.log(row.valueOf().ID)
      var data_s = this.datepickertable3List[0];
      var data_e = this.datepickertable3List[1];

      console.log(data_s)
      console.log(data_e)

      var conditions3 = {
        "ID":row.valueOf().ID,
        "laycan_start": data_s,
        "laycan_end": data_e
      }

      console.log(conditions3)

      this.axios({
        method: "put",
        url: "http://202.120.32.222:8888/users/tc_date",
        data:conditions3
      })
        .then(function (response) {
          window.location.reload(true);


        }

        )
        .catch(function (error) {
          console.log(error);
        });


      },


    // ton复选框选择 筛选EXCEL
    handleSelectionChange(val) {
        this.multipleSelection = val;
    },
    displaySelection(){

      console.log("%%%%");
      console.log( this.multipleSelection)

      var array = new Array();
      var arr = new Array();
      for(var i=0;i<this.multipleSelection.length;i++) {
         array.push(this.multipleSelection[i].ID)
         for(var j=0;j<this.tableData1.length;j++){
           if(this.multipleSelection[i].ID==this.tableData1[j].ID) {
               arr.push(this.tableData1[j])
             }
           }
      }
      console.log(array)
      console.log(arr)
      this.tableData1= arr
     },

    // cargo复选框选择 筛选EXCEL
    handleSelectionChange2(val) {
        this.multipleSelection2 = val;
    },
    displaySelection2(){

      console.log("%%%%");
      console.log( this.multipleSelection2)

      var array = new Array();
      var arr = new Array();
      for(var i=0;i<this.multipleSelection2.length;i++) {
         array.push(this.multipleSelection2[i].ID)
         for(var j=0;j<this.tableData2.length;j++){
           if(this.multipleSelection2[i].ID==this.tableData2[j].ID) {
               arr.push(this.tableData2[j])
             }
           }
      }
      console.log(array)
      console.log(arr)
      this.tableData2= arr
     },

    // tc复选框选择 筛选EXCEL
    handleSelectionChange3(val) {
        this.multipleSelection3 = val;
    },
    displaySelection3(){

      console.log("%%%%");
      console.log( this.multipleSelection3)

      var array = new Array();
      var arr = new Array();
      for(var i=0;i<this.multipleSelection3.length;i++) {
         array.push(this.multipleSelection3[i].ID)
         for(var j=0;j<this.tableData3.length;j++){
           if(this.multipleSelection3[i].ID==this.tableData3[j].ID) {
               arr.push(this.tableData3[j])
             }
           }
      }
      console.log(array)
      console.log(arr)
      this.tableData3= arr
     },




  }
};
</script>


<style>

/*!* 导出按钮 *!*/
/*.toexcel {*/
  /*cursor: pointer;*/
  /*cursor: hand;*/
  /*width: 70px;*/
  /*height: 34px;*/
/*}*/



.el-header {
  background-color: #66b1ff;
  color: #060606;
  text-align: center;
  line-height: 60px;
}
.el-footer {
  background-color: rgba(191, 195, 214, 0.04);
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
  color: #c7c3b2;
  text-align: center;
  line-height: 20px;
}
body > .el-container {
  margin-bottom: 40px;
}
.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 60px;
}
.el-container:nth-child(7) .el-aside {
  line-height: 10px;
}
</style>
