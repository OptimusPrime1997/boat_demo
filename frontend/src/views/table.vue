<template>


<el-container>
  <!--<el-aside width="220px">Other msg</el-aside>-->
  <el-container>
    <el-header>Boat Demo</el-header>
    <el-main>
        <el-row :gutter="20">
              <el-col :span="17">
                      <el-tabs v-model="activeName2" type="card" @tab-click="handleClick">
                          <el-tab-pane label="Tonnage Cards" name="first">

                                   <div>Tonnage offer cards</div>
                                   <div >
                                        <!--Vessel Name 搜索框的实现-->
                                        <div class="search_tonnage" style="text-align:left; display:inline ;float:left">
                                            Vessel Name :
                                            <input id="searchText1" type="text" class="searchBox" style="width:200px;height:25px;" />


                                        </div>

                                          <!--Sender's Mail 搜索框的实现-->
                                        <div class="search_tonnage" style="text-align:right; display:inline " >
                                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sender's Mail : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                            <input id="searchMail1" type="text" class="searchBox" style="width:200px;height:25px;"  />

                                        </div>
                                   </div>

                                   <div >

                                        <!--Open Date 日期框的实现-->
                                        <div id=tab1_data class="block" style="text-align:left;display:inline ;float:left ">
                                                <span class="demonstration" >Open Date : &nbsp;&nbsp;&nbsp;</span>
                                                <el-date-picker
                                                  v-model="value_a_1"
                                                  type="daterange"
                                                  range-separator="--"
                                                  start-placeholder="Start Date"
                                                  end-placeholder="End Date" style="height:30px;" >
                                                </el-date-picker>
                                        </div>

                                         <!--Sent within 框的实现-->
                                        <div style="text-align:left;display:inline " >
                                               &nbsp;&nbsp;Sent within : &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;
                                               <el-select v-model="value_a_2" placeholder="All" >
                                                  <el-option
                                                    v-for="item in options_a_2"
                                                    :key="item.value_a_2"
                                                    :label="item.label"
                                                    :value="item.value_a_2">
                                                  </el-option>
                                                </el-select>
                                                Days.

                                        </div>
                                   </div>

                                   <div>
                                         <!--Built 框的实现-->
                                        <div style="text-align:left ;display:inline ;float:left" >
                                               Built : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Under
                                               <el-select v-model="value_a_3" placeholder="All" >
                                                  <el-option
                                                    v-for="item in options_a_3"
                                                    :key="item.value_a_3"
                                                    :label="item.label"
                                                    :value="item.value_a_3">
                                                  </el-option>
                                                </el-select>
                                                Year(s).

                                        </div>

                                         <!--Mail Account 框的实现-->
                                        <div style="text-align:left;display:inline ;" >
                                               Mail Account :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                               <el-select v-model="value_a_4" placeholder="All" >
                                                  <el-option
                                                    v-for="item in options_a_4"
                                                    :key="item.value_a_4"
                                                    :label="item.label"
                                                    :value="item.value_a_4">
                                                  </el-option>
                                                </el-select>

                                        </div>
                                   </div>

                                   <div style="height: 50px">
                                         <!--Built 框的实现-->
                                        <div style="text-align:left ;display:inline ;float:left" >
                                               DWT :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                               <el-select v-model="value_a_5" placeholder="All" >
                                                  <el-option
                                                    v-for="item in options_a_5"
                                                    :key="item.value_a_5"
                                                    :label="item.label"
                                                    :value="item.value_a_5">
                                                  </el-option>
                                                </el-select>

                                        </div>

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


                                    <button @click="searchCargo1" class="btn" style="text-align:center;width:60px;height:32px;font-size:15px"  >Search</button>


                                    <div>

                                    <el-table
                                      :data="tableData1"
                                      height="800"
                                      border
                                      style="width: 100%"
                                      @row-click="display_mail">

                                              <el-table-column prop="Vessel_name" label="Vessel Name" width="200" >
                                              </el-table-column>

                                              <el-table-column prop="DWT" label="DWT" width="80"> </el-table-column>

                                              <el-table-column prop="BLT" label="BLT" width="80"> </el-table-column>

                                              <el-table-column prop="Open_area" label="Open Area" width="200">
                                              </el-table-column>

                                              <el-table-column prop="Open_date_S" label="Open Date Start" width="130">
                                              </el-table-column>
                                              <el-table-column prop="Open_date_E" label="Open Date End" width="130">
                                              </el-table-column>
                                              <el-table-column prop="Sent" label="Sent" width="80">
                                              </el-table-column>

                                    </el-table>


                                     <!--// 处理分页-->
                                     <el-pagination
                                        @size-change="handleSizeChange"
                                        @current-change="handleCurrentChange"
                                        :current-page="currentPage"
                                        :page-sizes="[10, 20, 30, 40]"
                                        :page-size="pageSize"
                                        layout="total, sizes, prev, next, jumper"
                                        :total="totalCount"
                                      ></el-pagination>
                                       </div>


                            </el-tab-pane>



                          <el-tab-pane label="Cargo Cards " name="second" >

                                    <div> Cargo offer cards</div>
                                      <div >

                                            <div class="search_cago"  style="text-align:left; display:inline ;float:left" >
                                                Cargo Name :
                                                <input id="searchText2" type="text" class="searchBox" style="width:200px;height:25px;"/>


                                            </div>


                                              <!--Sender's Mail 搜索框的实现-->
                                            <div class="search_tonnage" style="text-align:right; display:inline ">
                                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sender's Mail : &nbsp;&nbsp;&nbsp;&nbsp;
                                                <input id="searchMail2" type="text" class="searchBox" style="width:200px;height:25px;" />

                                            </div>
                                       </div>

                                       <div >

                                            <!--Laycan 日期框的实现-->
                                            <div class="block" style="text-align:left;display:inline ;float:left ">
                                                    <span class="demonstration" >Laycan : &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;</span>
                                                    <el-date-picker
                                                      v-model="value_b_1"
                                                      type="daterange"
                                                      range-separator="--"
                                                      start-placeholder="Start Date"
                                                      end-placeholder="End Date" style="height:30px;">
                                                    </el-date-picker>
                                            </div>

                                             <!--Sent within 框的实现-->
                                            <div style="text-align:left;display:inline " >
                                                   &nbsp;&nbsp;Sent within : &nbsp;&nbsp; &nbsp;&nbsp;
                                                   <el-select v-model="value_b_2" placeholder="All">
                                                      <el-option
                                                        v-for="item in options_b_2"
                                                        :key="item.value_b_2"
                                                        :label="item.label"
                                                        :value="item.value_b_2">
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
                                            <div style="text-align:left;display:inline ;" >
                                                   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mail Account :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                   <el-select v-model="value_b_4" placeholder="All">
                                                      <el-option
                                                        v-for="item in options_b_4"
                                                        :key="item.value_b_4"
                                                        :label="item.label"
                                                        :value="item.value_b_4">
                                                      </el-option>
                                                    </el-select>

                                            </div>
                                       <!--</div>-->
                                       <!--<div>-->

                                             <!--Qiantity 框的实现-->
                                            <div style="text-align:left ;display:inline ;float:left" >
                                                   Quantity :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                   <el-select v-model="value_b_5" placeholder="All">
                                                      <el-option
                                                        v-for="item in options_b_5"
                                                        :key="item.value_b_5"
                                                        :label="item.label"
                                                        :value="item.value_b_5">
                                                      </el-option>
                                                    </el-select>

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

                                       <button @click="searchCargo2" class="btn"  style="text-align:center;width:60px;height:32px;font-size:15px" >Search</button>





                                    <el-table :data="tableData2" height="800" border style="width: 100%" @row-click="display_mail">
                                    <el-table-column prop="Cargo_name" label="Cargo Name" width="130">
                                    </el-table-column>

                                    <el-table-column prop="Quantity" label="Quantity" width="130">
                                    </el-table-column>

                                    <el-table-column prop="Loading_Port" label="Loading Port" width="130">
                                    </el-table-column>

                                    <el-table-column
                                      prop="Discharging_Port"
                                      label="Discharging Port"
                                      width="180"
                                    >
                                    </el-table-column>

                                    <el-table-column prop="LayCan_S" label="LayCan_Start" width="130">
                                    </el-table-column>
                                    <el-table-column prop="LayCan_E" label="LayCan_End" width="130">
                                    </el-table-column>

                                    <el-table-column prop="Sent" label="Sent" width="130">
                                    </el-table-column>


                                  </el-table>

                                    <!--// 处理分页-->
                                     <el-pagination
                                        @size-change="handleSizeChange"
                                        @current-change="handleCurrentChange"
                                        :current-page="currentPage"
                                        :page-sizes="[10, 20, 30, 40]"
                                        :page-size="pageSize"
                                        layout="total, sizes, prev, next, jumper"
                                        :total="totalCount"
                                      ></el-pagination>


                            </el-tab-pane >






                          <el-tab-pane label="TC Cards" name="third" >
                                  <div>TC offer cards</div>
                                      <div>
                                            <div class="search_cago" style="text-align:left;display:inline ;float:left">
                                                Account : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                <input id="searchText3" type="text" class="searchBox" style="width:200px;height:25px;" />

                                            </div>



                                              <!--Sender's Mail 搜索框的实现-->
                                            <div class="search_tonnage" style="text-align:right; display:inline ">
                                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sender's Mail : &nbsp;&nbsp;&nbsp;&nbsp;
                                                <input id="searchMail3" type="text" class="searchBox" style="width:200px;height:25px;" />

                                            </div>
                                       </div>

                                       <div >

                                            <!--Laycan 日期框的实现-->
                                            <div class="block" style="text-align:left;display:inline ;float:left ">
                                                    <span class="demonstration" >Laycan : &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;</span>
                                                    <el-date-picker
                                                      v-model="value_c_1"
                                                      type="daterange"
                                                      range-separator="--"
                                                      start-placeholder="Start Date"
                                                      end-placeholder="End Date" style="height:30px;">
                                                    </el-date-picker>
                                            </div>

                                             <!--Sent within 框的实现-->
                                            <div style="text-align:left;display:inline " >
                                                   &nbsp;&nbsp;Sent within :  &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;
                                                   <el-select v-model="value_c_2" placeholder="All">
                                                      <el-option
                                                        v-for="item in options_b_2"
                                                        :key="item.value_c_2"
                                                        :label="item.label"
                                                        :value="item.value_c_2">
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
                                            <div style="text-align:left;display:inline ;" >
                                                   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mail Account :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                   <el-select v-model="value_c_4" placeholder="All">
                                                      <el-option
                                                        v-for="item in options_c_4"
                                                        :key="item.value_c_4"
                                                        :label="item.label"
                                                        :value="item.value_c_4">
                                                      </el-option>
                                                    </el-select>

                                            </div>
                                       <!--</div>-->
                                       <!--<div>-->

                                             <!--Qiantity 框的实现-->
                                            <div style="text-align:left ;display:inline ;float:left" >
                                                   Quantity :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                   <el-select v-model="value_c_5" placeholder="All">
                                                      <el-option
                                                        v-for="item in options_c_5"
                                                        :key="item.value_c_5"
                                                        :label="item.label"
                                                        :value="item.value_c_5">
                                                      </el-option>
                                                    </el-select>

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

                                    <button @click="searchCargo3" class="btn" style="text-align:center;width:60px;height:32px;font-size:15px">Search</button>

                                    <el-table :data="tableData3" height="800" border style="width: 100%" @row-click="display_mail">
                                            <el-table-column prop="Account" label="Account" width="130">
                                            </el-table-column>
                                            <el-table-column prop="Quantity" label="Quantity" width="150">
                                            </el-table-column>
                                            <el-table-column prop="Delivery_area" label="Delivery Area" width="130">
                                            </el-table-column>
                                            <el-table-column
                                              prop="Redelivery_area"
                                              label="Redelivery Area"
                                              width="130"
                                            >
                                            </el-table-column>

                                            <el-table-column prop="LayCan_S" label="LayCan Start" width="110">
                                            </el-table-column>
                                            <el-table-column prop="LayCan_E" label="LayCan End" width="110">
                                            </el-table-column>
                                            <el-table-column prop="DUR" label="DUR" width="80"> </el-table-column>
                                            <el-table-column prop="Sent" label="Sent" width="80">
                                            </el-table-column>
                                    </el-table>

                                     <!--// 处理分页-->
                                     <el-pagination
                                        @size-change="handleSizeChange"
                                        @current-change="handleCurrentChange"
                                        :current-page="currentPage"
                                        :page-sizes="[10, 20, 30, 40]"
                                        :page-size="pageSize"
                                        layout="total, sizes, prev, next, jumper"
                                        :total="totalCount"
                                      ></el-pagination>


                          </el-tab-pane>






                      </el-tabs>
              </el-col>


              <el-col :span="7">
                          <el-tabs type="border-card">
                              <el-tab-pane label="Mail">
                                <!-- talbe行 点击 获取邮件方法的实现-->
                                <div style = "overflow-x:hidden ;height:650px">

                                    <v-clamp autoresize :max-lines="10">{{text}}</v-clamp>
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
    import VClamp from 'vue-clamp'
    export default {
      data() {
        return {
          activeName2: 'first',
          tableData1: [],
          tableData2: [],
          tableData3: [],
          text: '',

          //存储分页，搜索数据

          params:{
            page:1,
            pageSize:3,
            categoryId:undefined,
            keywords:undefined
          },


        //定义Open Date日期的组件js部分
          value_a_1: '',

          //定义Sent within的组件js部分
          options_a_2: [{
                  value_a_2: '选项0',
                  label: 'All'
                },{
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
                },{
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
                },{
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
                },{
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
        // tonnage talbe行 点击方法
        display_mail(row) {
          // console.log("display mail method");
          // console.log(row['mail_text']);
          this.text = row['mail_text']

        },


        // 搜素框方法
        searchCargo1() {
          var self = this;
          this.tableData1.splice(0, this.tableData1.length);
          var data1 = new Array();
          var searchText1 = document.getElementById("searchText1").value;
          console.log(searchText1);
          //console.log(searchText.text);

          // var data1_1 = new Array();
          // var tab1_data = document.getElementById("tab1_data").value;
          //  console.log(ddddddddddddddd);
          // console.log(tab1_data);

          // if (searchText1) {
            this.axios({
              method: "get",
              url: "http://127.0.0.1:8888/users/search_tonnage/" + searchText1,
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
              })
              .catch(function (error) {
                console.log(error);
              });
            return data1;
          // }else if(tab1_data){
          //   this.axios({
          //     method: "get",
          //     url: "http://127.0.0.1:8888/users/search_tonnage/" + search_tonnage_data,
          //   })
          //     .then(function (response) {
          //       console.log("axios method");
          //       console.log(response);
          //       console.log(eval(response.data));
          //       // self.tableData2.splice(0, tableData1.length);
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
          //   return data1_1;




          //}



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







        // dj() {
        //   var self = this;
        //   this.axios({
        //     method: "get",
        //     url: "http://127.0.0.1:8888/users/search_cargo/"
        //   })
        //     .then(function (response) {
        //       console.log("axios method");
        //       console.log(response);
        //       console.log(eval(response.data));
        //       var a = eval(response.data);
        //       for (var i = 0; i < a.list.length; i++) {
        //         self.tableData2.push(a.list[i].fields);
        //         //JSON.stringify(a.list[i].fields)
        //       }
        //       console.log(self.tableData2);
        //       //this.tableData1.splice(xxx,xxx,xxx);
        //     })
        //     .catch(function (error) {
        //       console.log(error);
        //     });
        // },
        handleClick(tab, event) {
          console.log(tab, event);
        },

        //处理分页

         // 每页显示数据变更
         handleSizeChange(val) {
            // console.log("每页" + val + "条");
            //this.pageSize 是请求表格数据接口中的参数 设置表格每页显示多少条数据
            this.pageSize = val;
            this.loadTableData(); //调表格数据的接口
         },
         // 页码变更
         handleCurrentChange(val) {
           // console.log("当前页" + val);
           //this.currentPage 是请求表格数据接口中的参数 设置表格当前处于多少页
           this.currentPage = val;
           this.loadTableData();
         },



      }
    };
</script>


<style>
  .el-header{
    background-color: #66b1ff;
    color: #303133;
    text-align: center;
    line-height: 60px;
  }
  .el-footer{
    background-color: rgba(191, 195, 214, 0.04);
    color: #333;
    text-align: center;
    line-height:60px;
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

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 60px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 10px;
  }












</style>
