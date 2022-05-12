CREATE DATABASE IF NOT EXISTS pixivtj
USE pixivtj
CREATE TABLE IF NOT EXISTS User(
    userId char(10) NOT NULL PRIMARY key,
    name VARCHAR(100),
    image VARCHAR(500),
    imageBig VARCHAR(500),
    premium BOOLEAN,
    isFollowed BOOLEAN,
    isMypixiv BOOLEAN,
    isBlocking BOOLEAN,
    background VARCHAR(500),
)

CREATE TABLE IF NOT EXISTS illust(
    illustid varchar(10),
    illustTitle varchar(500),
    illustComment varchar(5000),
    id varchar(10),
    title varchar(500),
    description varchar(5000),
    illustType int,
    createDate datetime,
    uploadDate datetime,
    restrict int,
    xRestrict int,
    sl int,
    url_min varchar(50),
    url_thumb varchar(50),
    url_samll varchar(50),
    url_regular varchar(50),
    url_original varchar(50),
    alt varchar(500),
    userId varchar(10),
    userName varcahr(100),
    userAccount varchar(100),
    likeData BOOLEAN,
    width int,
    height int,
    pageCount int,
    bookmarkCount int,
    likeCount int,
    commentCount int,
    responseCount int,
    viewCount int,
    bookStyle int,
    isHowto BOOLEAN,
    isOriginal BOOLEAN,
    ImageResponseCount int,
)

CREATE TABLE IF NOT EXISTS tag(
    tag varchar(100),
    locked BOOLEAN,
    deletable BOOLEAN,
    userId varchar(10),
    tanslation_name varchar(100),
    userName varchar(100)
)