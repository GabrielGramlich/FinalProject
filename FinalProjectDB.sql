-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema FinalProjectDB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema FinalProjectDB
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `FinalProjectDB` ;
CREATE SCHEMA IF NOT EXISTS `FinalProjectDB` DEFAULT CHARACTER SET utf8 ;
USE `FinalProjectDB` ;

-- -----------------------------------------------------
-- Table `FinalProjectDB`.`Races`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`Races` (
  `RaceID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`RaceID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`Backgrounds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`Backgrounds` (
  `BackgroundID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`BackgroundID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`Classes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`Classes` (
  `ClassID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `HitPoints` INT NOT NULL,
  `Skills` INT NOT NULL,
  PRIMARY KEY (`ClassID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`AbilityScores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`AbilityScores` (
  `AbilityScoreID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`AbilityScoreID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`Features`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`Features` (
  `FeatureID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `Description` VARCHAR(1000) NOT NULL,
  PRIMARY KEY (`FeatureID`),
  UNIQUE INDEX `FeaturesID_UNIQUE` (`FeatureID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`Languages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`Languages` (
  `LanguageID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`LanguageID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`Proficiencies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`Proficiencies` (
  `ProficiencyID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(25) NOT NULL,
  `Type` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`ProficiencyID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`AbilityScoreBridge`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`AbilityScoreBridge` (
  `AbilityScoreBridgeID` INT NOT NULL AUTO_INCREMENT,
  `Modifier` INT NOT NULL,
  `AbilityScoreID` INT NOT NULL,
  `RaceID` INT NOT NULL,
  PRIMARY KEY (`AbilityScoreBridgeID`),
  INDEX `fk_AbilityScoreBridge_AbilityScores_idx` (`AbilityScoreID` ASC) VISIBLE,
  INDEX `fk_AbilityScoreBridge_Races1_idx` (`RaceID` ASC) VISIBLE,
  CONSTRAINT `fk_AbilityScoreBridge_AbilityScores`
    FOREIGN KEY (`AbilityScoreID`)
    REFERENCES `FinalProjectDB`.`AbilityScores` (`AbilityScoreID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_AbilityScoreBridge_Races1`
    FOREIGN KEY (`RaceID`)
    REFERENCES `FinalProjectDB`.`Races` (`RaceID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`LanguageBridge`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`LanguageBridge` (
  `LanguageBridgeID` INT NOT NULL AUTO_INCREMENT,
  `LanguageID` INT NOT NULL,
  `RaceID` INT NULL,
  `BackgroundID` INT NULL,
  `Choice` TINYINT NOT NULL,
  PRIMARY KEY (`LanguageBridgeID`),
  INDEX `fk_LanguageBridge_Languages1_idx` (`LanguageID` ASC) VISIBLE,
  INDEX `fk_LanguageBridge_Races1_idx` (`RaceID` ASC) VISIBLE,
  INDEX `fk_LanguageBridge_Backgrounds1_idx` (`BackgroundID` ASC) VISIBLE,
  CONSTRAINT `fk_LanguageBridge_Languages1`
    FOREIGN KEY (`LanguageID`)
    REFERENCES `FinalProjectDB`.`Languages` (`LanguageID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_LanguageBridge_Races1`
    FOREIGN KEY (`RaceID`)
    REFERENCES `FinalProjectDB`.`Races` (`RaceID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_LanguageBridge_Backgrounds1`
    FOREIGN KEY (`BackgroundID`)
    REFERENCES `FinalProjectDB`.`Backgrounds` (`BackgroundID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`ProficiencyBridge`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`ProficiencyBridge` (
  `ProficiencyBridgeID` INT NOT NULL AUTO_INCREMENT,
  `ProficiencyID` INT NOT NULL,
  `BackgroundID` INT NULL,
  `ClassID` INT NULL,
  `RaceID` INT NULL,
  `Choice` TINYINT NULL,
  PRIMARY KEY (`ProficiencyBridgeID`),
  INDEX `fk_ProficiencyBridge_Proficiencies1_idx` (`ProficiencyID` ASC) VISIBLE,
  INDEX `fk_ProficiencyBridge_Backgrounds1_idx` (`BackgroundID` ASC) VISIBLE,
  INDEX `fk_ProficiencyBridge_Classes1_idx` (`ClassID` ASC) VISIBLE,
  INDEX `fk_ProficiencyBridge_Races1_idx` (`RaceID` ASC) VISIBLE,
  CONSTRAINT `fk_ProficiencyBridge_Proficiencies1`
    FOREIGN KEY (`ProficiencyID`)
    REFERENCES `FinalProjectDB`.`Proficiencies` (`ProficiencyID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ProficiencyBridge_Backgrounds1`
    FOREIGN KEY (`BackgroundID`)
    REFERENCES `FinalProjectDB`.`Backgrounds` (`BackgroundID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ProficiencyBridge_Classes1`
    FOREIGN KEY (`ClassID`)
    REFERENCES `FinalProjectDB`.`Classes` (`ClassID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ProficiencyBridge_Races1`
    FOREIGN KEY (`RaceID`)
    REFERENCES `FinalProjectDB`.`Races` (`RaceID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`FeatureBridge`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`FeatureBridge` (
  `FeatureBridgeID` INT NOT NULL AUTO_INCREMENT,
  `FeatureID` INT NOT NULL,
  `BackgroundID` INT NULL,
  `ClassID` INT NULL,
  `RaceID` INT NULL,
  PRIMARY KEY (`FeatureBridgeID`),
  INDEX `fk_FeaturesBridge_Features1_idx` (`FeatureID` ASC) VISIBLE,
  INDEX `fk_FeaturesBridge_Backgrounds1_idx` (`BackgroundID` ASC) VISIBLE,
  INDEX `fk_FeaturesBridge_Classes1_idx` (`ClassID` ASC) VISIBLE,
  INDEX `fk_FeaturesBridge_Races1_idx` (`RaceID` ASC) VISIBLE,
  CONSTRAINT `fk_FeaturesBridge_Features1`
    FOREIGN KEY (`FeatureID`)
    REFERENCES `FinalProjectDB`.`Features` (`FeatureID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FeaturesBridge_Backgrounds1`
    FOREIGN KEY (`BackgroundID`)
    REFERENCES `FinalProjectDB`.`Backgrounds` (`BackgroundID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FeaturesBridge_Classes1`
    FOREIGN KEY (`ClassID`)
    REFERENCES `FinalProjectDB`.`Classes` (`ClassID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FeaturesBridge_Races1`
    FOREIGN KEY (`RaceID`)
    REFERENCES `FinalProjectDB`.`Races` (`RaceID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`Armor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`Armor` (
  `ArmorID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(25) NOT NULL,
  `Base` INT NOT NULL,
  `Type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ArmorID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`ArmorBridge`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`ArmorBridge` (
  `ArmorBridgeID` INT NOT NULL AUTO_INCREMENT,
  `ArmorID` INT NOT NULL,
  `ClassID` INT NOT NULL,
  PRIMARY KEY (`ArmorBridgeID`),
  INDEX `fk_ArmorBridge_Armor1_idx` (`ArmorID` ASC) VISIBLE,
  INDEX `fk_ArmorBridge_Classes1_idx` (`ClassID` ASC) VISIBLE,
  CONSTRAINT `fk_ArmorBridge_Armor1`
    FOREIGN KEY (`ArmorID`)
    REFERENCES `FinalProjectDB`.`Armor` (`ArmorID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ArmorBridge_Classes1`
    FOREIGN KEY (`ClassID`)
    REFERENCES `FinalProjectDB`.`Classes` (`ClassID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`Weapons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`Weapons` (
  `WeaponID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(25) NOT NULL,
  `Damage` VARCHAR(10) NOT NULL,
  `Modifier` INT NOT NULL,
  PRIMARY KEY (`WeaponID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`WeaponBridge`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`WeaponBridge` (
  `WeaponBridgeID` INT NOT NULL AUTO_INCREMENT,
  `WeaponID` INT NOT NULL,
  `ClassID` INT NOT NULL,
  `Amount` INT NOT NULL,
  PRIMARY KEY (`WeaponBridgeID`),
  INDEX `fk_WeaponBridge_Weapons1_idx` (`WeaponID` ASC) VISIBLE,
  INDEX `fk_WeaponBridge_Classes1_idx` (`ClassID` ASC) VISIBLE,
  CONSTRAINT `fk_WeaponBridge_Weapons1`
    FOREIGN KEY (`WeaponID`)
    REFERENCES `FinalProjectDB`.`Weapons` (`WeaponID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_WeaponBridge_Classes1`
    FOREIGN KEY (`ClassID`)
    REFERENCES `FinalProjectDB`.`Classes` (`ClassID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FinalProjectDB`.`SavingThrowBridge`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FinalProjectDB`.`SavingThrowBridge` (
  `SavingThrowID` INT NOT NULL AUTO_INCREMENT,
  `ClassID` INT NOT NULL,
  `AbilityScoreID` INT NOT NULL,
  PRIMARY KEY (`SavingThrowID`),
  INDEX `fk_SavingThrowBridge_Classes1_idx` (`ClassID` ASC) VISIBLE,
  INDEX `fk_SavingThrowBridge_AbilityScores1_idx` (`AbilityScoreID` ASC) VISIBLE,
  CONSTRAINT `fk_SavingThrowBridge_Classes1`
    FOREIGN KEY (`ClassID`)
    REFERENCES `FinalProjectDB`.`Classes` (`ClassID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_SavingThrowBridge_AbilityScores1`
    FOREIGN KEY (`AbilityScoreID`)
    REFERENCES `FinalProjectDB`.`AbilityScores` (`AbilityScoreID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
