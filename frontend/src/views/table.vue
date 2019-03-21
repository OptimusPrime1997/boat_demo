<template>


<el-container>
  <el-aside width="220px">Other msg</el-aside>
  <el-container>
    <el-header>Boat Demo</el-header>
    <el-main>
        <el-row :gutter="20">
              <el-col :span="19">
                      <el-tabs v-model="activeName2" type="card" @tab-click="handleClick">
                          <el-tab-pane label="Tonnage Cards" name="first">
                                    <div>Tonnage offer cards</div>
                                      <div class="search_tonnage" style="text-align:left">
                                          Vessel Name :
                                          <input id="searchText1" type="text" class="searchBox" />

                                      </div>

                                      <button @click="searchCargo1" class="btn" style="text-align:center;width:50px;height:21px">Search</button>


                                    <!--<div style="text-align:right" >-->
                                            <!--Open Area :-->
                                            <!--<input id="2" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:left" >-->
                                            <!--Sender's Mail :-->
                                            <!--<input id="3" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:right" >-->
                                           <!--DWT :-->
                                          <!--<input id="4" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:left" >-->
                                            <!--Open Date :-->
                                            <!--<input id="5" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:right" >-->
                                            <!--Built :-->
                                            <!--<input id="6" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                     <!--<div style="text-align:left" >-->
                                            <!--Mail Account :-->
                                            <!--<input id="7" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:right" >-->
                                            <!--Sent within :-->
                                            <!--<input id="8" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div>  <button  class="btn">搜 索</button></div>-->



                                    <el-table
                                              :data="tableData1"
                                              height="350"
                                              border
                                              style="width: 100%"  @row-click="display_mail">

                                              <el-table-column prop="Vessel_name" label="Vessel Name" width="200">
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



                            </el-tab-pane>




                          <el-tab-pane label="Cargo Cards " name="second" >

                                    <div> Cargo offer cards</div>

                                      <div class="search_cago"  style="text-align:left">
                                          Cargo Name :
                                          <input id="searchText2" type="text" class="searchBox" />

                                      </div>


                                      <button @click="searchCargo2" class="btn"  style="text-align:center;width:50px;height:21px">Search</button>




                                    <!--<div style="text-align:right" >-->
                                            <!--Quantity :-->
                                            <!--<input id="22" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:left" >-->
                                            <!--Loading Port :-->
                                            <!--<input id="23" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:right" >-->
                                           <!--Disch.Port :-->
                                          <!--<input id="24" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:left" >-->
                                            <!--Laycan :-->
                                            <!--<input id="25" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:right" >-->
                                            <!--Sender's Mail:-->
                                            <!--<input id="26" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                     <!--<div style="text-align:left" >-->
                                            <!--Mail Account :-->
                                            <!--<input id="27" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:right" >-->
                                            <!--Sent within :-->
                                            <!--<input id="28" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div>  <button  class="btn">搜 索</button></div>-->




                                    <el-table :data="tableData2" height="320" border style="width: 100%" @row-click="display_mail">
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


                            </el-tab-pane >



                          <el-tab-pane label="TC Cards" name="third" >
                                  <div>TC offer cards</div>
                                      <div class="search_cago" style="text-align:left">
                                          Account :
                                          <input id="searchText3" type="text" class="searchBox" />
                                      </div>



                                      <button @click="searchCargo3" class="btn" style="text-align:center;width:50px;height:21px">Search</button>

                                    <!--<div style="text-align:left" >-->
                                         <!--Account :-->
                                        <!--<input id="31" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:right" >-->
                                            <!--Quantity :-->
                                            <!--<input id="32" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:left" >-->
                                            <!--Del.Area :-->
                                            <!--<input id="33" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:right" >-->
                                           <!--Redel. Area :-->
                                          <!--<input id="34" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:left" >-->
                                            <!--Laycan :-->
                                            <!--<input id="35" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:right" >-->
                                            <!--Duration :-->
                                            <!--<input id="36" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                     <!--<div style="text-align:left" >-->
                                            <!--Sender's Mail :-->
                                            <!--<input id="37" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:right" >-->
                                            <!--Sent within :-->
                                            <!--<input id="38" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div style="text-align:left" >-->
                                            <!--Mail Account :-->
                                            <!--<input id="39" type="text" class="searchBox" />-->

                                    <!--</div>-->

                                    <!--<div>  <button  class="btn">搜 索</button></div>-->

                                    <el-table :data="tableData3" height="320" border style="width: 100%" @row-click="display_mail">
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

                          </el-tab-pane>


                      </el-tabs>
              </el-col>


              <el-col :span="5">
                          <el-tabs type="border-card">
                              <el-tab-pane label="Mail">
                                <div style = "overflow-x:hidden ;height:500px">

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
          text: ''
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
          this.axios({
            method: "get",
            url: "http://127.0.0.1:8888/users/search_tonnage/" + searchText1,
          })
            .then(function (response) {
              console.log("axios method");
              console.log(response);
              console.log(eval(response.data));
              // self.tableData2.splice(0, tableData1.length);
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
    color: #00ff00;
    text-align: center;
    line-height: 700px;
  }

  .el-main {
    background-color: rgba(214, 57, 67, 0.01);
    color: #5ec262;
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
