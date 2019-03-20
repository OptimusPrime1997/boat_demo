<template>
  <el-tabs v-model="activeName2" type="card" @tab-click="handleClick">
    <el-tab-pane label="Tonnage Cards" name="first">
      <div>Tonnage offer cards</div>

      <el-table :data="tableData1" height="250" border style="width: 100%">
        <el-table-column prop="Vessel_name" label="Vessel Name" width="180">
        </el-table-column>

        <el-table-column prop="DWT" label="DWT" width="180"> </el-table-column>

        <el-table-column prop="BLT" label="BLT" width="180"> </el-table-column>

        <el-table-column prop="Open_area" label="Open Area" width="180">
        </el-table-column>

        <el-table-column prop="Open_Date_S" label="Open Date Start" width="180">
        </el-table-column>
        <el-table-column prop="Open_Date_E" label="Open Date End" width="180">
        </el-table-column>
        <el-table-column prop="Sent" label="Sent" width="180">
        </el-table-column>
      </el-table>
    </el-tab-pane>

    <el-tab-pane label="Cargo Cards " name="second">
      <div>Cargo offer cards</div>

      <div class="search_cago">
        <input id="searchText" type="text" class="searchBox" />
        <button @click="searchCargo" class="btn">搜 索</button>
      </div>

      <el-table :data="tableData2" height="250" border style="width: 100%">
        <el-table-column prop="Cargo_name" label="Cargo Name" width="180">
        </el-table-column>

        <el-table-column prop="Quantity" label="Quantity" width="180">
        </el-table-column>

        <el-table-column prop="Loading_Port" label="Loading Port" width="180">
        </el-table-column>

        <el-table-column
          prop="Discharging_Port"
          label="Discharging Port"
          width="180"
        >
        </el-table-column>

        <el-table-column prop="LayCan_S" label="LayCan_Start" width="180">
        </el-table-column>
        <el-table-column prop="LayCan_E" label="LayCan_End" width="180">
        </el-table-column>

        <el-table-column prop="Sent" label="Sent" width="180">
        </el-table-column>
      </el-table>
    </el-tab-pane>

    <el-tab-pane label="TC Cards" name="third">
      <div>TC offer cards</div>

      <el-table :data="tableData3" height="250" border style="width: 100%">
        <el-table-column prop="Account" label="Account" width="180">
        </el-table-column>
        <el-table-column prop="Quantity" label="Quantity" width="180">
        </el-table-column>
        <el-table-column prop="Delivery_area" label="Delivery Area" width="180">
        </el-table-column>
        <el-table-column
          prop="Redelivery_area"
          label="Redelivery Area"
          width="180"
        >
        </el-table-column>

        <el-table-column prop="LayCan_S" label="LayCan Start" width="180">
        </el-table-column>
        <el-table-column prop="LayCan_E" label="LayCan End" width="180">
        </el-table-column>
        <el-table-column prop="DUR" label="DUR" width="180"> </el-table-column>
        <el-table-column prop="Sent" label="Sent" width="180">
        </el-table-column>
      </el-table>
    </el-tab-pane>
  </el-tabs>
</template>


<script>
export default {
  data() {
    return {
      activeName2: 'first',
      tableData1: [],
      tableData2: [],
      tableData3: []
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
    searchCargo() {
      var self = this;
      this.tableData2.splice(0, this.tableData2.length);
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

    dj() {
      var self = this;
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
            self.tableData2.push(a.list[i].fields);
            //JSON.stringify(a.list[i].fields)
          }
          console.log(self.tableData2);
          //this.tableData1.splice(xxx,xxx,xxx);
        })
        .catch(function (error) {
          console.log(error);
        });

    },

    handleClick(tab, event) {
      console.log(tab, event);
    },
  }
};

</script>
