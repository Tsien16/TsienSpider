create table administrative_division
(
    id          int          not null comment '自增主键'
        primary key,
    area_code   varchar(255) null comment '行政区域代码',
    area_name   varchar(255) null comment '行政区域名称',
    area_level  varchar(255) null comment '行政区划级别',
    parent_code varchar(255) null comment '上级行政区域',
    ur_code     varchar(255) null comment '城乡分类代码'
)
    comment '行政区划表';

