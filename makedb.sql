CREATE DATABASE IF NOT EXISTS pixivtj;
USE pixivtj;
CREATE TABLE IF NOT EXISTS User(
    userId VARCHAR(10) NOT NULL PRIMARY KEY,
    name VARCHAR(100),
    image VARCHAR(500),
    imageBig VARCHAR(500),
    premium BOOLEAN,
    isFollowed BOOLEAN,
    isMypixiv BOOLEAN,
    isBlocking BOOLEAN,
    background VARCHAR(500)
);
CREATE TABLE IF NOT EXISTS Illust(
    illustid VARCHAR(10) NOT NULL PRIMARY KEY,
    illustTitle VARCHAR(500),
    illustComment VARCHAR(5000),
    id VARCHAR(10),
    title VARCHAR(500),
    description VARCHAR(5000),
    illustType INT,
    createDate DATETIME,
    uploadDate DATETIME,
    pixiv_restrict INT,
    xRestrict INT,
    sl INT,
    url_min VARCHAR(50),
    url_thumb VARCHAR(50),
    url_samll VARCHAR(50),
    url_regular VARCHAR(50),
    url_original VARCHAR(50),
    alt VARCHAR(500),
    userId VARCHAR(10),
    userName VARCHAR(100),
    userAccount VARCHAR(100),
    likeData BOOLEAN,
    width INT,
    height INT,
    pageCount INT,
    bookmarkCount INT,
    likeCount INT,
    commentCount INT,
    responseCount INT,
    viewCount INT,
    bookStyle INT,
    isHowto BOOLEAN,
    isOriginal BOOLEAN,
    ImageResponseCount INT
);

CREATE TABLE IF NOT EXISTS Tag(
    tag VARCHAR(100),
    locked BOOLEAN,
    deletable BOOLEAN,
    userId VARCHAR(10),
    tanslation_name VARCHAR(100),
    userName VARCHAR(100)
);