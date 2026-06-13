---
entity_id: "molecule.ecocyc.CA_2"
entity_type: "small_molecule"
name: "Ca2+"
source_database: "EcoCyc"
source_id: "CA+2"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "calcium(II)"
  - "Ca++"
  - "calcium ion"
  - "CaII"
---

# Ca2+

`molecule.ecocyc.CA_2`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:CA+2`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

EcoCyc compound CA+2

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s). Binds pyrimidine-specific ribonucleoside hydrolase RihB (complex.ecocyc.CPLX0-7904), outer membrane phospholipase A (complex.ecocyc.CPLX0-7944), ATP-dependent helicase/uracil glycosylase Lhr (complex.ecocyc.CPLX0-8581), glycerophosphoryl diester phosphodiesterase, periplasmic (complex.ecocyc.GLYCPDIESTER-PERI-CPLX), NADH:quinone oxidoreductase I (complex.ecocyc.NADH-DHI-CPLX), malS (protein.P25718), ralR (protein.P33229), mtgA (protein.P46022), and 2 more.

## Annotation

EcoCyc compound CA+2

## Outgoing Edges (44)

- `activates` --> [[reaction.ecocyc.3.4.15.5-RXN|reaction.ecocyc.3.4.15.5-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.GDPMANDEHYDRA-RXN|reaction.ecocyc.GDPMANDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.MANNONOXIDOREDUCT-RXN|reaction.ecocyc.MANNONOXIDOREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.PEPCARBOXYKIN-RXN|reaction.ecocyc.PEPCARBOXYKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.PEPDEPHOS-RXN|reaction.ecocyc.PEPDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN0-7100|reaction.ecocyc.RXN0-7100]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.SAMDECARB-RXN|reaction.ecocyc.SAMDECARB-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `binds` --> [[complex.ecocyc.CPLX0-7904|complex.ecocyc.CPLX0-7904]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-7944|complex.ecocyc.CPLX0-7944]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-8581|complex.ecocyc.CPLX0-8581]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.GLYCPDIESTER-PERI-CPLX|complex.ecocyc.GLYCPDIESTER-PERI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.NADH-DHI-CPLX|complex.ecocyc.NADH-DHI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P25718|protein.P25718]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P33229|protein.P33229]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P46022|protein.P46022]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P75804|protein.P75804]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P76407|protein.P76407]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-144|reaction.ecocyc.TRANS-RXN-144]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-144|reaction.ecocyc.TRANS-RXN-144]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.3.1.27.6-RXN|reaction.ecocyc.3.1.27.6-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.325-BISPHOSPHATE-NUCLEOTIDASE-RXN|reaction.ecocyc.325-BISPHOSPHATE-NUCLEOTIDASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ACID-PHOSPHATASE-RXN|reaction.ecocyc.ACID-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ADENPRIBOSYLTRAN-RXN|reaction.ecocyc.ADENPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ADENYLATECYC-RXN|reaction.ecocyc.ADENYLATECYC-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CHEYDEPHOS-RXN|reaction.ecocyc.CHEYDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `represses` --> [[reaction.ecocyc.D-PPENTOMUT-RXN|reaction.ecocyc.D-PPENTOMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DIACYLGLYKIN-RXN|reaction.ecocyc.DIACYLGLYKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN|reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLYCDEH-RXN|reaction.ecocyc.GLYCDEH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN|reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.INORGPYROPHOSPHAT-RXN|reaction.ecocyc.INORGPYROPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.KDO-8PPHOSPHAT-RXN|reaction.ecocyc.KDO-8PPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.METHYLISOCITRATE-LYASE-RXN|reaction.ecocyc.METHYLISOCITRATE-LYASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PEPDEPHOS-RXN|reaction.ecocyc.PEPDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSPHAGLYPSYN-RXN|reaction.ecocyc.PHOSPHAGLYPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PRPPSYN-RXN|reaction.ecocyc.PRPPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-22463|reaction.ecocyc.RXN-22463]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-9514|reaction.ecocyc.RXN-9514]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-4181|reaction.ecocyc.RXN0-4181]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5120|reaction.ecocyc.RXN0-5120]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-6527|reaction.ecocyc.RXN0-6527]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRIPHOSPHATASE-RXN|reaction.ecocyc.TRIPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN|reaction.ecocyc.UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:CA+2`
- `METANETX:MNXM128`
- `BIGG:ca2`
- `METABOLIGHTS:MTBLC29108`
- `HMDB:HMDB00464`
- `CHEMSPIDER:266`
- `PUBCHEM:271`
- `LIGAND-CPD:C00076`
- `CHEBI:29108`

## Notes

(CA 1)
