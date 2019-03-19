<template>
<div>
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane label="Tonnage Cards" name="first" >
                    <div > Tonnage offer cards </div>

                    <div>

                            <tr>
                              <td><label htmlFor='username'>Vessel Name :</label></td>
                              <td><input type="text" id='username'/></td>
                            </tr>

                    </div>
                    <div>
                             <tr>
                               <td><label htmlFor='usermail'>Sender's Mail :</label></td>
                               <td><input type="text" id='usermail'/></td>
                             </tr>
                    </div>
                   <div>
                              <div style='float:left'> Open Area : </div>
                              <div style='float:left'>
                                <el-select v-model="value8" filterable placeholder="None">
                                  <el-option
                                    v-for="item in options"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                  </el-option>
                                </el-select>
                              </div>
                               <el-select style='float:left'
                                  v-model="value9"
                                  multiple
                                  filterable
                                  remote
                                  reserve-keyword
                                  placeholder="请输入关键词"
                                  :remote-method="remoteMethod"
                                  :loading="loading">
                                  <el-option
                                    v-for="item in options4"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                  </el-option>
                                </el-select>


                   </div>
                     </br></br></br></br>
                   <div >
                             <div class="block" >
                              <span class="demonstration" style='float:left'>Open Date：</span>
                              <el-date-picker
                                style='float:left'
                                v-model="value7"
                                type="datetimerange"
                                align="right"
                                start-placeholder="开始日期"
                                end-placeholder="结束日期"
                                :default-time="['12:00:00', '08:00:00']">
                              </el-date-picker>
                            </div>

                   </div>
                    </br></br></br></br>
                    <div style='float:left'> DWT: </div>
                    <div>


                             <el-select v-model="value" placeholder="All" style='float:left'>
                                <el-option
                                  v-for="item in options1"
                                  :key="item.value"
                                  :label="item.label"
                                  :value="item.value">
                                </el-option>
                              </el-select>


                    </div>
                     </br></br></br></br>
                    <div style='float:left' > Built: </div>
                    <div style='float:left'> Under </div>

                    <div>
                           <el-select v-model="value4" clearable placeholder="All" style='float:left'>
                              <el-option
                                v-for="item in options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                              </el-option>
                            </el-select>

                    </div>

                    <div style='float:left'> Year(s) </div>
                    </br></br></br></br>

                     <div style='float:left'> Sent within: </div>
                     <div>
                          <el-select v-model="value6" placeholder="All" style='float:left'>
                              <el-option
                                v-for="item in days"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                                <span style="float: left">{{ item.label }}</span>
                                <span style="float: right; color: #8492a6; font-size: 13px">{{ item.value }}</span>
                              </el-option>
                            </el-select>

                     </div>
                     <div style='float:left'> Days </div>
                      </br></br></br></br>

                     <div style='float:left'>Mail Account: </div>

            <div>
                          <el-select v-model="value6" placeholder="All" style='float:left'>
                              <el-option
                                v-for="item in mails"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                                <span style="float: left">{{ item.label }}</span>
                                <span style="float: right; color: #8492a6; font-size: 13px">{{ item.value }}</span>
                              </el-option>
                            </el-select>
            </div>


          </el-tab-pane>







          <el-tab-pane label="Cargo Cards " name="second">
                  <div> Cargo offer cards </div>

                    <div>

                            <tr>
                              <td><label >Cargo Name :</label></td>
                              <td><input type="text" id='username1'/></td>
                            </tr>

                    </div>
                    <div>
                             <tr>
                               <td><label htmlFor='usermail'>Sender's Mail :</label></td>
                               <td><input type="text" id='usermail'/></td>
                             </tr>
                    </div>
                   <div>
                              <div style='float:left'> Loading Port : </div>
                              <div style='float:left'>
                                <el-select v-model="value8" filterable placeholder="None">
                                  <el-option
                                    v-for="item in options"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                  </el-option>
                                </el-select>
                              </div>
                               <el-select style='float:left'
                                  v-model="value9"
                                  multiple
                                  filterable
                                  remote
                                  reserve-keyword
                                  placeholder="请输入关键词"
                                  :remote-method="remoteMethod"
                                  :loading="loading">
                                  <el-option
                                    v-for="item in options4"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                  </el-option>
                                </el-select>


                   </div>
                      </br></br></br></br>
                    <div>
                              <div style='float:left'> Disch. Port : </div>
                              <div style='float:left'>
                                <el-select v-model="value8" filterable placeholder="None">
                                  <el-option
                                    v-for="item in options"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                  </el-option>
                                </el-select>
                              </div>
                               <el-select style='float:left'
                                  v-model="value9"
                                  multiple
                                  filterable
                                  remote
                                  reserve-keyword
                                  placeholder="请输入关键词"
                                  :remote-method="remoteMethod"
                                  :loading="loading">
                                  <el-option
                                    v-for="item in options4"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                  </el-option>
                                </el-select>


                   </div>


                     </br></br></br></br>
                   <div >
                             <div class="block" >
                              <span class="demonstration" style='float:left'>Laycan：</span>
                              <el-date-picker
                                style='float:left'
                                v-model="value7"
                                type="datetimerange"
                                align="right"
                                start-placeholder="开始日期"
                                end-placeholder="结束日期"
                                :default-time="['12:00:00', '08:00:00']">
                              </el-date-picker>
                            </div>

                   </div>
                    </br></br></br></br>
                    <div style='float:left'> Quantity: </div>
                    <div>


                             <el-select v-model="value" placeholder="All" style='float:left'>
                                <el-option
                                  v-for="item in options1"
                                  :key="item.value"
                                  :label="item.label"
                                  :value="item.value">
                                </el-option>
                              </el-select>


                    </div>



                    </br></br></br></br>

                     <div style='float:left'> Sent within: </div>
                     <div>
                          <el-select v-model="value6" placeholder="All" style='float:left'>
                              <el-option
                                v-for="item in days"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                                <span style="float: left">{{ item.label }}</span>
                                <span style="float: right; color: #8492a6; font-size: 13px">{{ item.value }}</span>
                              </el-option>
                            </el-select>

                     </div>
                     <div style='float:left'> Days </div>
                      </br></br></br></br>

                     <div style='float:left'>Mail Account: </div>

            <div>
                          <el-select v-model="value6" placeholder="All" style='float:left'>
                              <el-option
                                v-for="item in mails"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                                <span style="float: left">{{ item.label }}</span>
                                <span style="float: right; color: #8492a6; font-size: 13px">{{ item.value }}</span>
                              </el-option>
                            </el-select>
            </div>


          </el-tab-pane>









          <el-tab-pane label="TC Cards" name="third">
                    <div> TC offer cards </div>

                    <div>

                            <tr>
                              <td><label htmlFor='username1'>Account :</label></td>
                              <td><input type="text" id='username1'/></td>
                            </tr>

                    </div>
                    <div>
                             <tr>
                               <td><label htmlFor='usermail'>Sender's Mail :</label></td>
                               <td><input type="text" id='usermail'/></td>
                             </tr>
                    </div>
                   <div>
                              <div style='float:left'> Del.Area: </div>
                              <div style='float:left'>
                                <el-select v-model="value8" filterable placeholder="None">
                                  <el-option
                                    v-for="item in options"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                  </el-option>
                                </el-select>
                              </div>
                               <el-select style='float:left'
                                  v-model="value9"
                                  multiple
                                  filterable
                                  remote
                                  reserve-keyword
                                  placeholder="请输入关键词"
                                  :remote-method="remoteMethod"
                                  :loading="loading">
                                  <el-option
                                    v-for="item in options4"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                  </el-option>
                                </el-select>


                   </div>
                      </br></br></br></br>
                    <div>
                              <div style='float:left'> Redel.Area : </div>
                              <div style='float:left'>
                                <el-select v-model="value8" filterable placeholder="None">
                                  <el-option
                                    v-for="item in options"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                  </el-option>
                                </el-select>
                              </div>
                               <el-select style='float:left'
                                  v-model="value9"
                                  multiple
                                  filterable
                                  remote
                                  reserve-keyword
                                  placeholder="请输入关键词"
                                  :remote-method="remoteMethod"
                                  :loading="loading">
                                  <el-option
                                    v-for="item in options4"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                  </el-option>
                                </el-select>


                   </div>


                     </br></br></br></br>
                   <div >
                             <div class="block" >
                              <span class="demonstration" style='float:left'>Laycan：</span>
                              <el-date-picker
                                style='float:left'
                                v-model="value7"
                                type="datetimerange"
                                align="right"
                                start-placeholder="开始日期"
                                end-placeholder="结束日期"
                                :default-time="['12:00:00', '08:00:00']">
                              </el-date-picker>
                            </div>

                   </div>
                    </br></br></br></br>
                    <div style='float:left'> Quantity: </div>
                    <div>


                             <el-select v-model="value" placeholder="All" style='float:left'>
                                <el-option
                                  v-for="item in options1"
                                  :key="item.value"
                                  :label="item.label"
                                  :value="item.value">
                                </el-option>
                              </el-select>


                    </div>



                    </br></br></br></br>

                     <div style='float:left'> Sent within: </div>
                     <div>
                          <el-select v-model="value6" placeholder="All" style='float:left'>
                              <el-option
                                v-for="item in days"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                                <span style="float: left">{{ item.label }}</span>
                                <span style="float: right; color: #8492a6; font-size: 13px">{{ item.value }}</span>
                              </el-option>
                            </el-select>

                     </div>
                     <div style='float:left'> Days </div>
                      </br></br></br></br>

                     <div style='float:left'>Mail Account: </div>

            <div>
                          <el-select v-model="value6" placeholder="All" style='float:left'>
                              <el-option
                                v-for="item in mails"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                                <span style="float: left">{{ item.label }}</span>
                                <span style="float: right; color: #8492a6; font-size: 13px">{{ item.value }}</span>
                              </el-option>
                            </el-select>
            </div>



          </el-tab-pane>
        </el-tabs>















</div>

</template>

<script>
export default {
  data() {
    return {
      activeName: 'second',

      options: [{
          value: '选项1',
          label: '1 Days'
        }, {
          value: '选项2',
          label: '2 Days'
        }, {
          value: '选项3',
          label: '3 Days'
        }, {
          value: '选项4',
          label: '5 Days'
        }, {
          value: '选项5',
          label: '7 Days'
        }, {
          value: '选项6',
          label: '10 Days'
        }, {
          value: '选项7',
          label: '15 Days'
        }],
        value8: '',

        options4: [],
        value9: [],
        list: [],
        loading: false,
        states: ["Alabama", "Alaska", "Arizona",
        "Arkansas", "California", "Colorado",
        "Connecticut", "Delaware", "Florida",
        "Georgia", "Hawaii", "Idaho", "Illinois",
        "Indiana", "Iowa", "Kansas", "Kentucky",
        "Louisiana", "Maine", "Maryland",
        "Massachusetts", "Michigan", "Minnesota",
        "Mississippi", "Missouri", "Montana",
        "Nebraska", "Nevada", "New Hampshire",
        "New Jersey", "New Mexico", "New York",
        "North Carolina", "North Dakota", "Ohio",
        "Oklahoma", "Oregon", "Pennsylvania",
        "Rhode Island", "South Carolina",
        "South Dakota", "Tennessee", "Texas",
        "Utah", "Vermont", "Virginia",
        "Washington", "West Virginia", "Wisconsin",
        "Wyoming"],

        value7: '',

         options1: [{
          value: '选项1',
          label: 'Small Handy(0-10000)'
        }, {
          value: '选项2',
          label: 'Handy(10000-40000)'
        }, {
          value: '选项3',
          label: 'Large Handy(35000-40000)'
        }, {
          value: '选项4',
          label: 'Handy Max(40000-50000)'
        }, {
          value: '选项5',
          label: 'Supra Max(40000-50000)'
        },
        {
          value: '选项6',
          label: 'Pana Max(65000-100000)'
        },
        {
          value: '选项7',
          label: 'Post PMX(90000-100000)'
        },
        {
          value: '选项8',
          label: 'Afra Max(75000-115000)'
        },
        {
          value: '选项9',
          label: 'Cape(100000-450000)'
        },
        {
          value: '选项10',
          label: 'VLCC(150000-320000)'
        },
        {
          value: '选项11',
          label: 'ULCC(320000-550000)'
        }

        ],
        value: '',

        options: [{
          value: '选项1',
          label: '5'
        }, {
          value: '选项2',
          label: '10'
        }, {
          value: '选项3',
          label: '15'
        }, {
          value: '选项4',
          label: '20'
        }, {
          value: '选项5',
          label: '25'
        },
        {
          value: '选项6',
          label: '30'
        }],
        value4: '',

        days: [{
          value: 'One',
          label: '1'
        }, {
          value: 'Two',
          label: '2'
        }, {
          value: 'Three',
          label: '3'
        }, {
          value: 'Four',
          label: '4'
        }, {
          value: 'Five',
          label: '5'
        },
        {
          value: 'Six',
          label: '6'
        },{
          value: 'Seven',
          label: '7'
        }],
        value4: '',

                mails: [{
          value: '',
          label: 'All'
        }, {
          value: '',
          label: 'moses'
        }],
        value4: ''








    }
  },
  methods: {

      handleClick(tab, event) {
        console.log(tab, event);
      },
      remoteMethod(query) {
        if (query !== '') {
          this.loading = true;
          setTimeout(() => {
            this.loading = false;
            this.options4 = this.list.filter(item => {
              return item.label.toLowerCase()
                .indexOf(query.toLowerCase()) > -1;
            });
          }, 200);
        } else {
          this.options4 = [];
        }
      }
    },
    mounted() {
      this.list = this.states.map(item => {
        return { value: item, label: item };
      });
    }
}
</script>

