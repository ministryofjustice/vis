@sea: rgb(234, 235, 245);
@pcc_fill: #fff;
@pcc_border: rgb(53, 69, 101);
@pcc_line_width: 1.2;

@outline: #999;
@outline_highlight: #666;

Map {
  background-color: rgb(234, 235, 245);
}

#data, #london {
  polygon-fill: @pcc_fill;
  polygon-smooth: 1.0;
  line-width: @pcc_line_width;
  line-color: @pcc_border;
  line-smooth: 1;
  line-simplify: 1.0;
}


#data[name='Northern Ireland'],
#data[name='City Of London'] {
  polygon-opacity: 0;
  raster-opacity: 0;
  line-opacity: 0;
}
