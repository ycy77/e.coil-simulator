---
entity_id: "molecule.ecocyc.CU_2"
entity_type: "small_molecule"
name: "Cu2+"
source_database: "EcoCyc"
source_id: "CU+2"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "Cu++"
  - "cupric ion"
  - "cupric copper"
  - "copper(II)"
  - "CuII"
---

# Cu2+

`molecule.ecocyc.CU_2`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:CU+2`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

EcoCyc compound CU+2

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s). Binds copper-containing amine oxidase (complex.ecocyc.AMINEOXID-CPLX), cytochrome bo3 ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-O-UBIOX-CPLX), sodC (protein.P0AGD1), cueO (protein.P36649), ypdE (protein.P77585).

## Annotation

EcoCyc compound CU+2

## Outgoing Edges (58)

- `activates` --> [[reaction.ecocyc.RXN0-1483|reaction.ecocyc.RXN0-1483]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `binds` --> [[complex.ecocyc.AMINEOXID-CPLX|complex.ecocyc.AMINEOXID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CYT-O-UBIOX-CPLX|complex.ecocyc.CYT-O-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P0AGD1|protein.P0AGD1]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P36649|protein.P36649]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P77585|protein.P77585]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.RXN0-2945|reaction.ecocyc.RXN0-2945]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-639|reaction.ecocyc.TRANS-RXN0-639]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.R170-RXN|reaction.ecocyc.R170-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7363|reaction.ecocyc.RXN0-7363]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-639|reaction.ecocyc.TRANS-RXN0-639]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.1.1.1.283-RXN|reaction.ecocyc.1.1.1.283-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.3-NUCLEOTID-RXN|reaction.ecocyc.3-NUCLEOTID-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.3.4.15.5-RXN|reaction.ecocyc.3.4.15.5-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.4.3.1.17-RXN|reaction.ecocyc.4.3.1.17-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.7-ALPHA-HYDROXYSTEROID-DEH-RXN|reaction.ecocyc.7-ALPHA-HYDROXYSTEROID-DEH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ACETYLORNDEACET-RXN|reaction.ecocyc.ACETYLORNDEACET-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ACETYLORNTRANSAM-RXN|reaction.ecocyc.ACETYLORNTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.AKBLIG-RXN|reaction.ecocyc.AKBLIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ALLANTOINASE-RXN|reaction.ecocyc.ALLANTOINASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.AMINOPROPDEHYDROG-RXN|reaction.ecocyc.AMINOPROPDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.AMYLOMALT-RXN|reaction.ecocyc.AMYLOMALT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CROBETREDUCT-RXN|reaction.ecocyc.CROBETREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CYCPHOSDIESTER-RXN|reaction.ecocyc.CYCPHOSDIESTER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CYTDEAM-RXN|reaction.ecocyc.CYTDEAM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.D-PPENTOMUT-RXN|reaction.ecocyc.D-PPENTOMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GALACTUROISOM-RXN|reaction.ecocyc.GALACTUROISOM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUCUROISOM-RXN|reaction.ecocyc.GLUCUROISOM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTDECARBOX-RXN|reaction.ecocyc.GLUTDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTSEMIALDEHYDROG-RXN|reaction.ecocyc.GLUTSEMIALDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLYCDEH-RXN|reaction.ecocyc.GLYCDEH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLYCOLATEDEHYDRO-RXN|reaction.ecocyc.GLYCOLATEDEHYDRO-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLYCOPHOSPHORYL-RXN|reaction.ecocyc.GLYCOPHOSPHORYL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLYOCARBOLIG-RXN|reaction.ecocyc.GLYOCARBOLIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLYOXII-RXN|reaction.ecocyc.GLYOXII-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLYOXIII-RXN|reaction.ecocyc.GLYOXIII-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GUANOSINEKIN-RXN|reaction.ecocyc.GUANOSINEKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.INOSINEKIN-RXN|reaction.ecocyc.INOSINEKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.KDO-8PPHOSPHAT-RXN|reaction.ecocyc.KDO-8PPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.KDO-8PSYNTH-RXN|reaction.ecocyc.KDO-8PSYNTH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.LACTALDDEHYDROG-RXN|reaction.ecocyc.LACTALDDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MANNOSE-ISOMERASE-RXN|reaction.ecocyc.MANNOSE-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.N-ACETYLGLUTPREDUCT-RXN|reaction.ecocyc.N-ACETYLGLUTPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.N-ACETYLTRANSFER-RXN|reaction.ecocyc.N-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PGLUCONDEHYDRAT-RXN|reaction.ecocyc.PGLUCONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.POLYPHOSPHATE-KINASE-RXN|reaction.ecocyc.POLYPHOSPHATE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-14249|reaction.ecocyc.RXN-14249]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-22463|reaction.ecocyc.RXN-22463]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-22575|reaction.ecocyc.RXN-22575]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-1139|reaction.ecocyc.RXN0-1139]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-299|reaction.ecocyc.RXN0-299]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5120|reaction.ecocyc.RXN0-5120]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-6676|reaction.ecocyc.RXN0-6676]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7390|reaction.ecocyc.RXN0-7390]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7399|reaction.ecocyc.RXN0-7399]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7489|reaction.ecocyc.RXN0-7489]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN|reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TETHYDPICSUCC-RXN|reaction.ecocyc.TETHYDPICSUCC-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P76278|protein.P76278]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:CU+2`
- `LIGAND-CPD:C22424`
- `SEED:cpd00058`
- `METANETX:MNXM632`
- `BIGG:cu2`
- `HMDB:HMDB00657`
- `CHEMSPIDER:25221`
- `PUBCHEM:27099`
- `CHEBI:29036`

## Notes

(CU 1)
