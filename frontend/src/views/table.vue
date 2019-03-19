<template>
  <el-tabs v-model="activeName2" type="card" @tab-click="handleClick">
    <el-tab-pane label="Tonnage Cards" name="first">
      <div>Tonnage offer cards</div>

      <el-table
        :data="tableData1"
        height="250"
        border
        style="width: 100%">

        <el-table-column
          prop="Vessel_Name"
          label="Vessel Name"
          width="180">
        </el-table-column>

        <el-table-column
          prop="DWT"
          label="DWT"
          width="180">
        </el-table-column>

        <el-table-column
          prop="BLT"
          label="BLT"
          width="180">
        </el-table-column>

        <el-table-column
          prop="Open_Area"
          label="Open Area"
          width="180">
        </el-table-column>

        <el-table-column
          prop="Open_Date"
          label="Open Date"
          width="180">
        </el-table-column>

        <el-table-column
          prop="Sent"
          label="Sent"
          width="180">
        </el-table-column>


      </el-table>

    </el-tab-pane>


    <el-tab-pane label="Cargo Cards " name="second">
      <div> Cargo offer cards</div>

      <div class="search_cago">
        <input id="searchText" type="text" class="searchBox">
        <button @click="searchCargo" class="btn">搜 索</button>
      </div>


      <el-table
        :data="tableData2"
        height="250"
        border
        style="width: 100%">

        <el-table-column
          prop="Cargo_Name"
          label="Cargo Name"
          width="180">
        </el-table-column>

        <el-table-column
          prop="Quantity"
          label="Quantity"
          width="180">
        </el-table-column>

        <el-table-column
          prop="Loading_Port"
          label="Loading Port"
          width="180">
        </el-table-column>

        <el-table-column
          prop="Discharging_Port"
          label="Discharging Port"
          width="180">
        </el-table-column>

        <el-table-column
          prop="LayCan"
          label="LayCan"
          width="180">
        </el-table-column>

        <el-table-column
          prop="Sent"
          label="Sent"
          width="180">
        </el-table-column>


      </el-table>

    </el-tab-pane>


    <el-tab-pane label="TC Cards" name="third">
      <div>TC offer cards</div>

      <el-table
        :data="tableData3"
        height="250"
        border
        style="width: 100%">

        <el-table-column
          prop="Account"
          label="Account"
          width="180">
        </el-table-column>

        <el-table-column
          prop="Quantity"
          label="Quantity"
          width="180">
        </el-table-column>

        <el-table-column
          prop="Delivery_Area"
          label="Delivery Area"
          width="180">
        </el-table-column>

        <el-table-column
          prop="Redelivery_Area"
          label="Redelivery Area"
          width="180">
        </el-table-column>

        <el-table-column
          prop="LayCan"
          label="LayCan"
          width="180">
        </el-table-column>

        <el-table-column
          prop="DUR"
          label="DUR"
          width="180">
        </el-table-column>

        <el-table-column
          prop="Sent"
          label="Sent"
          width="180">
        </el-table-column>


      </el-table>

    </el-tab-pane>


  </el-tabs>
</template>


<script>
  export default {

    name: "search",
    model: {
      props: "tableData2"
    },
    props: {
      tableData2: {
        type: String
      }
    },
    data() {
      var tableData2 = new Array();
      this.axios({
        method: "get",
        url: "http://127.0.0.1:8888/users/cargo"
      })
        .then(function (response) {
          console.log("axios method");
          console.log(response);
          console.log(eval(response.data));
          var a = eval(response.data);

          for (var i = 0; i < a.list.length; i++) {
            tableData2.push(a.list[i].fields);
            //JSON.stringify(a.list[i].fields)
          }
          console.log(tableData2);
          //this.tableData1.splice(xxx,xxx,xxx);
        })
        .catch(function (error) {
          console.log(error);
        });

      var tableData1 = new Array();
      this.axios({
        method: "get",
        url: "http://127.0.0.1:8888/users/tonnage"
      })
        .then(function (response) {
          console.log("axios method");
          console.log(response);
          console.log(eval(response.data));
          var a = eval(response.data);

          for (var i = 0; i < a.list.length; i++) {
            tableData1.push(a.list[i].fields);
            //JSON.stringify(a.list[i].fields)
          }
          console.log(tableData1);
          //this.tableData1.splice(xxx,xxx,xxx);
        })
        .catch(function (error) {
          console.log(error);
        });

      var tableData3 = new Array();
      this.axios({
        method: "get",
        url: "http://127.0.0.1:8888/users/tc"
      })
        .then(function (response) {
          console.log("axios method");
          console.log(response);
          console.log(eval(response.data));
          var a = eval(response.data);

          for (var i = 0; i < a.list.length; i++) {
            tableData3.push(a.list[i].fields);
            //JSON.stringify(a.list[i].fields)
          }
          console.log(tableData3);
          //this.tableData1.splice(xxx,xxx,xxx);
        })
        .catch(function (error) {
          console.log(error);
        });

      console.log("test");
      console.log("test");

      return {
        activeName2: 'first',

        tableData1: tableData1,

        tableData2: tableData2,

        tableData3: tableData3


      };
    },

    watch() {
      console.log("watch function");
      tableData2:searchCargo();
    },


    methods: {
      searchCargo() {
        var data2 = new Array();
        var searchText = document.getElementById("searchText").value;
        console.log(searchText);
        //console.log(searchText.text);
        this.axios({
          method: "get",
          url: "http://127.0.0.1:8888/users/search_cargo/" + searchText,
        })
          .then(function (response) {
            console.log("axios method");
            console.log(response);
            console.log(eval(response.data));
            var a = eval(response.data);
            for (var i = 0; i < a.list.length; i++) {
              data2.push(a.list[i].fields);
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

      dj: function () {
        this.axios({
          method: "get",
          url: "http://127.0.0.1:8888/users/search_cargo/"
        })
          .then(function (response) {
            console.log("axios method");
            console.log(response);
            console.log(eval(response.data));
            var a = eval(response.data);

            for (var i = 0; i < a.list.length; i++) {
              tableData2.push(a.list[i].fields);
              //JSON.stringify(a.list[i].fields)
            }
            console.log(tableData2);
            //this.tableData1.splice(xxx,xxx,xxx);
          })
          .catch(function (error) {
            console.log(error);
          });

      },

      handleClick(tab, event) {
        console.log(tab, event);
      },

      mounted: function () {
        console.log("mounted");
        console.log("updateTable1");
        this.axios({
          method: "get",
          url: "http://127.0.0.1:8888/users/cargo"
        })
          .then(function (response) {
            console.log("axios method");
            data = response.data;
            console.log(data);

            //this.tableData1.splice(xxx,xxx,xxx);
          })
          .catch(function (error) {
            console.log(error);
          });


      },

    }
  };

</script>
