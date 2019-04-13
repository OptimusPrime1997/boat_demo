<!--<template>-->
    <!--<section>-->
        <!--&lt;!&ndash;工具条&ndash;&gt;-->
        <!--<el-col :span="24" class="toolbar" style="padding-bottom: 0px;">-->
            <!--<el-button v-if="editOk"  type="success" @click="btnOk" size="small" icon="el-icon-circle-check-outline">保存</el-button>-->
            <!--<el-button v-else="editOk" type="primary"  @click="btnEdit" size="small" icon="el-icon-edit">编辑</el-button>-->
        <!--</el-col>-->
        <!--<el-table :data="tableData" style="width: 100%">-->
            <!--<el-table-column label="日期" width="180">-->
                <!--<template slot-scope="scope">-->
                    <!--<span>{{scope.row.date}}</span>-->
                <!--</template>-->
            <!--</el-table-column>-->
            <!--<el-table-column prop="name" label="姓名">-->
                <!--<template slot-scope="scope">-->
                    <!--<span>{{scope.row.name}}</span>-->
                <!--</template>-->
            <!--</el-table-column>-->
            <!--<el-table-column prop="address" label="地址">-->
                <!--<template slot-scope="scope">-->
                    <!--<template  v-if="editOk">-->
                        <!--<el-input class="edit-input" size="small" v-model="scope.row.address"></el-input>-->
                    <!--</template>-->
                    <!--<span v-else>{{ scope.row.address }}</span>-->
                <!--</template>-->
            <!--</el-table-column>-->
        <!--</el-table>-->
    <!--</section>-->
<!--</template>-->
<!--<script>-->
  <!--export default {-->
    <!--data() {-->
      <!--return {-->
        <!--tableData: [{-->
            <!--id:'1',-->
            <!--date: '2016-05-02',-->
            <!--name: '王小虎',-->
            <!--address: '上海市普陀区金沙江路 1518 弄',-->
        <!--}, {-->
            <!--id:'2',-->
            <!--date: '2016-05-04',-->
            <!--name: '王小虎',-->
            <!--address: '上海市普陀区金沙江路 1517 弄',-->
        <!--}, {-->
            <!--id:'3',-->
            <!--date: '2016-05-01',-->
            <!--name: '王小虎',-->
            <!--address: '上海市普陀区金沙江路 1519 弄',-->
        <!--}, {-->
            <!--id:'4',-->
            <!--date: '2016-05-03',-->
            <!--name: '王小虎',-->
            <!--address: '上海市普陀区金沙江路 1516 弄',-->
        <!--}],-->
        <!--editOk:false-->
      <!--}-->
    <!--},-->
    <!--methods: {-->
        <!--btnEdit(){-->
             <!--this.editOk=true;-->
        <!--},-->
        <!--btnOk(){-->
            <!--this.editOk=false;-->
        <!--}-->
    <!--}-->
  <!--}-->
<!--</script>-->


<!--<template>-->
    <!--<div class="TestWorld">-->
        <!--<el-table ref="multipleTable" :data="tableData3" tooltip-effect="dark"     style="width: 100%"  @selection-change="handleSelectionChange">-->
            <!--<el-table-column type="selection" width="55">-->
            <!--</el-table-column>-->
            <!--<el-table-column label="日期" width="120">-->
                <!--<template slot-scope="scope">{{ scope.row.date }}</template>-->
            <!--</el-table-column>-->
            <!--<el-table-column prop="name" label="姓名" width="120">-->
            <!--</el-table-column>-->
            <!--<el-table-column prop="address" label="地址" show-overflow-tooltip>-->
            <!--</el-table-column>-->
      <!--</el-table>-->
      <!--<div style="margin-top: 20px">-->
          <!--<el-button @click="batchDelete">批量删除</el-button>-->
          <!--<el-button @click="toggleSelection()">取消选择</el-button>-->
      <!--</div>-->
    <!--</div>-->

<!--</template>-->


<!--<script>-->

<!--export default {-->
    <!--name:'TestWorld',-->
    <!--data() {-->
        <!--return {-->
                <!--tableData3: [-->
                    <!--{-->
                      <!--date: '2016-05-03',-->
                      <!--name: '王小虎',-->
                      <!--address: '上海市普陀区金沙江路 1518 弄'-->
                    <!--},-->
                    <!--{-->
                      <!--date: '2016-05-02',-->
                      <!--name: '王小虎',-->
                      <!--address: '上海市普陀区金沙江路 1518 弄'-->
                    <!--},-->
                    <!--{-->
                      <!--date: '2016-05-04',-->
                      <!--name: '王小虎',-->
                      <!--address: '上海市普陀区金沙江路 1518 弄'-->
                    <!--},-->
                    <!--{-->
                      <!--date: '2016-05-01',-->
                      <!--name: '王小虎',-->
                      <!--address: '上海市普陀区金沙江路 1518 弄'-->
                    <!--},-->
                    <!--{-->
                      <!--date: '2016-05-08',-->
                      <!--name: '王小虎',-->
                      <!--address: '上海市普陀区金沙江路 1518 弄'-->
                    <!--},{-->
                      <!--date: '2016-05-06',-->
                      <!--name: '王小虎',-->
                      <!--address: '上海市普陀区金沙江路 1518 弄'-->
                    <!--},{-->
                      <!--date: '2016-05-07',-->
                      <!--name: '王小虎',-->
                      <!--address: '上海市普陀区金沙江路 1518 弄'-->
                    <!--}],-->
                    <!--multipleSelection: []-->
        <!--}-->
    <!--},-->
    <!--methods:{-->
        <!--toggleSelection(rows) {-->
           <!--if (rows) {-->
               <!--rows.forEach(row => {-->
               <!--this.$refs.multipleTable.toggleRowSelection(row);-->
           <!--});-->
           <!--} else {-->
               <!--this.$refs.multipleTable.clearSelection();-->
           <!--}-->
         <!--},-->
         <!--batchDelete(){-->
             <!--let  multData = this.multipleSelection;-->
             <!--let  tableData =this.tableData3;-->
             <!--let  multDataLen = multData.length;-->
             <!--let  tableDataLen = tableData.length;-->
             <!--for(let i = 0; i < multDataLen ;i++){-->
                 <!--for(let y=0;y < tableDataLen;y++){-->
                     <!--if(JSON.stringify(tableData[y]) == JSON.stringify(multData[i])){  //判断是否相等，相等就删除-->
                       <!--this.tableData3.splice(y,1)-->
                       <!--console.log("aa")-->
                     <!--}-->
                 <!--}-->
             <!--}-->
         <!--},-->
         <!--handleSelectionChange(val) {-->
           <!--this.multipleSelection = val;-->
         <!--}-->
    <!--}-->

<!--}-->



<!--</script>-->


<!--<template>-->
  <!--<div class="TestWord">-->
      <!--<el-button @click="addLine">添加行数</el-button>-->
      <!--<el-button @click="save">保存</el-button>-->
        <!--<el-table-->
          <!--:data="tableData"-->
          <!--style="width: 100%">-->
          <!--<el-table-column prop="bookname" label="书名">-->
             <!--<template slot-scope="scope">-->
             <!--<el-input v-model="scope.row.bookname" placeholder="书名"></el-input>-->
             <!--</template>-->
          <!--</el-table-column>-->
          <!--<el-table-column prop="bookvolume" label="册数">-->
             <!--<template slot-scope="scope">-->
             <!--<el-input v-model="scope.row.bookvolume" placeholder="册数"></el-input>-->
             <!--</template>-->
          <!--</el-table-column>-->
          <!--<el-table-column prop="bookbuyer" label="购买者">-->
             <!--<template slot-scope="scope">-->

             <!--<el-input v-model="scope.row.bookbuyer" placeholder="购买者"></el-input>-->
             <!--</template>-->
          <!--</el-table-column>-->
          <!--<el-table-column prop="bookborrower" label="借阅者">-->
             <!--<template slot-scope="scope">-->
             <!--<el-input v-model="scope.row.bookborrower" placeholder="借阅者"></el-input>-->
             <!--</template>-->
          <!--</el-table-column>-->
          <!--<el-table-column prop="bookbuytime" label="购买日期">-->
             <!--<template slot-scope="scope">-->
               <!--<el-date-picker-->
                 <!--v-model="scope.row.bookbuytime"-->
                 <!--type="date"-->
                 <!--format="yyyy-MM-dd"-->
                 <!--value-format="yyyy-MM-dd"-->
                 <!--placeholder="购买日期">-->
               <!--</el-date-picker>-->
             <!--</template>-->
          <!--</el-table-column>-->
          <!--<el-table-column prop="bookbuytime" label="购买日期">-->
             <!--<template slot-scope="scope">-->
               <!--<el-button-->
                  <!--size="mini"-->
                  <!--type="danger"-->
                  <!--v-if="!scope.row.editing"-->
                  <!--icon="el-icon-delete"-->
                  <!--@click="handleDelete(scope.$index, scope.row)">删除-->
               <!--</el-button>-->
             <!--</template>-->
          <!--</el-table-column>-->
    <!--</el-table>-->
  <!--</div>-->
<!--</template>-->
<!--<script>-->
<!--export default {-->
    <!--name:'TestWorld',-->
    <!--data() {-->
        <!--return {-->
            <!--tableData:[{-->
                <!--bookname: '',-->
                <!--bookbuytime: '',-->
                <!--bookbuyer: '',-->
                <!--bookborrower: '',-->
                <!--bookvolume:''-->
            <!--}]-->
        <!--}-->
    <!--},-->
    <!--methods:{-->
        <!--addLine(){ //添加行数-->
            <!--var newValue = {-->
                  <!--bookname: '',-->
                  <!--bookbuytime: '',-->
                  <!--bookbuyer: '',-->
                  <!--bookborrower: '',-->
                  <!--bookvolume:''-->
              <!--};-->
            <!--//添加新的行数-->
            <!--this.tableData.push(newValue);-->
        <!--},-->
        <!--handleDelete(index){ //删除行数-->
            <!--this.tableData.splice(index, 1)-->
        <!--},-->
        <!--save(){-->
          <!--//这部分应该是保存提交你添加的内容-->
          <!--console.log(JSON.stringify(this.tableData))-->
        <!--}-->
    <!--}-->

<!--}-->

<!--</script>-->



<!--<template>-->
    <!--<el-table :data="tableData" style="width: 100%">-->
        <!--<el-table-column label="日期" width="180">-->
            <!--<template slot-scope="scope">-->
                <!--<span>{{scope.row.date}}</span>-->
            <!--</template>-->
        <!--</el-table-column>-->
        <!--<el-table-column prop="name" label="姓名">-->
            <!--<template slot-scope="scope">-->
                <!--<span>{{scope.row.name}}</span>-->
            <!--</template>-->
        <!--</el-table-column>-->
        <!--<el-table-column prop="address" label="地址">-->
            <!--<template slot-scope="scope">-->
                <!--<template v-if="scope.row.edit">-->
                    <!--<el-input class="edit-input" size="small" v-model="scope.row.address"></el-input>-->
                <!--</template>-->
                <!--<span v-else>{{ scope.row.address }}</span>-->
            <!--</template>-->
        <!--</el-table-column>-->
        <!--<el-table-column label="操作">-->
            <!--<template slot-scope="scope">-->
                <!--<el-button v-if="scope.row.edit" type="success" @click="confirmEdit(scope.$index, scope.row)" size="small" icon="el-icon-circle-check-outline">保存</el-button>-->
                <!--<el-button v-else type="primary" @click='scope.row.edit=!scope.row.edit' size="small" icon="el-icon-edit">编辑</el-button>-->
            <!--</template>-->
        <!--</el-table-column>-->
    <!--</el-table>-->
<!--</template>-->

<!--<script>-->
  <!--export default {-->
    <!--data() {-->
      <!--return {-->
        <!--tableData: [{-->
            <!--id:'1',-->
            <!--date: '2016-05-02',-->
            <!--name: '王小虎',-->
            <!--address: '上海市普陀区金沙江路 1518 弄',-->
            <!--edit:false-->
        <!--}, {-->
            <!--id:'2',-->
            <!--date: '2016-05-04',-->
            <!--name: '王小虎',-->
            <!--address: '上海市普陀区金沙江路 1517 弄',-->
            <!--edit:false-->
        <!--}, {-->
            <!--id:'3',-->
            <!--date: '2016-05-01',-->
            <!--name: '王小虎',-->
            <!--address: '上海市普陀区金沙江路 1519 弄',-->
            <!--edit:false-->
        <!--}, {-->
            <!--id:'4',-->
            <!--date: '2016-05-03',-->
            <!--name: '王小虎',-->
            <!--address: '上海市普陀区金沙江路 1516 弄',-->
            <!--edit:false-->
        <!--}]-->
      <!--}-->
    <!--},-->
    <!--methods: {-->
        <!--confirmEdit(index,row){-->
            <!--row.edit = false;-->
            <!--this.$message({-->
                <!--message: '该地址已经成功修改',-->
                <!--type: 'success'-->
            <!--})-->
        <!--}-->
    <!--}-->
  <!--}-->
<!--</script>-->

