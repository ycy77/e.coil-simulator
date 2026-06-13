---
entity_id: "protein.P0A862"
entity_type: "protein"
name: "tpx"
source_database: "UniProt"
source_id: "P0A862"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:7499381}. Cytoplasm {ECO:0000269|PubMed:19054092}. Note=Forms a mixed disulfide with cytoplasmic thioredoxin (trx1). {ECO:0000269|PubMed:19054092}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tpx yzzJ b1324 JW1317"
---

# tpx

`protein.P0A862`

## Static

- Type: `protein`
- Source: `UniProt:P0A862`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:7499381}. Cytoplasm {ECO:0000269|PubMed:19054092}. Note=Forms a mixed disulfide with cytoplasmic thioredoxin (trx1). {ECO:0000269|PubMed:19054092}.

## Enriched Summary

FUNCTION: Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides. Has a preference for alkyl hydroperoxides and acts as a lipid peroxidase to inhibit bacterial membrane oxidation. Acts as a principal antioxidant during anaerobic growth. {ECO:0000255|HAMAP-Rule:MF_00269, ECO:0000269|PubMed:12514184, ECO:0000269|PubMed:14676195}. Tpx is a RED-THIOREDOXIN-MONOMER-dependent thiol peroxidase that belongs to the family of atypical 2-Cys peroxidases . In vivo, Tpx appears to function as a lipid hydroperoxide peroxidase and acts as the principal antioxidant under anaerobic conditions . Osmotic shock experiments initially indicated that the enzyme was located in the periplasm . However, no signal sequence for transport into the periplasm is evident, and in vivo interaction with RED-THIOREDOXIN-MONOMER indicates that the enzyme is located in the cytoplasm . Kinetic analysis shows a bisubstrate ping-pong catalytic mechanism . The enzyme is a dimer in solution, and this form is independent of the redox state; electrophoresis data is consistent with intrasubunit disulfide bond formation . A crystal structure of Tpx in the oxidized state has been solved at 2.2 Å resolution...

## Biological Role

Component of lipid hydroperoxide peroxidase (complex.ecocyc.CPLX0-7747).

## Annotation

FUNCTION: Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides. Has a preference for alkyl hydroperoxides and acts as a lipid peroxidase to inhibit bacterial membrane oxidation. Acts as a principal antioxidant during anaerobic growth. {ECO:0000255|HAMAP-Rule:MF_00269, ECO:0000269|PubMed:12514184, ECO:0000269|PubMed:14676195}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7747|complex.ecocyc.CPLX0-7747]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1324|gene.b1324]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A862`
- `KEGG:ecj:JW1317;eco:b1324;ecoc:C3026_07750;`
- `GeneID:75171449;75203439;945880;`
- `GO:GO:0005829; GO:0008379; GO:0032843; GO:0034599; GO:0042597`
- `EC:1.11.1.24`

## Notes

Thiol peroxidase (Tpx) (EC 1.11.1.24) (Peroxiredoxin tpx) (Prx) (Scavengase p20) (Thioredoxin peroxidase) (Thioredoxin-dependent peroxiredoxin)
