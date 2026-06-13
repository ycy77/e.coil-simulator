---
entity_id: "protein.P77444"
entity_type: "protein"
name: "sufS"
source_database: "UniProt"
source_id: "P77444"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sufS csdB ynhB b1680 JW1670"
---

# sufS

`protein.P77444`

## Static

- Type: `protein`
- Source: `UniProt:P77444`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Cysteine desulfurases mobilize the sulfur from L-cysteine to yield L-alanine, an essential step in sulfur metabolism for biosynthesis of a variety of sulfur-containing biomolecules. Component of the suf operon, which is activated and required under specific conditions such as oxidative stress and iron limitation. Acts as a potent selenocysteine lyase in vitro, that mobilizes selenium from L-selenocysteine. Selenocysteine lyase activity is however unsure in vivo. Can also desulfinate L-cysteine sulfinate (3-sulfino-L-alanine). {ECO:0000269|PubMed:10329673, ECO:0000269|PubMed:10829016, ECO:0000269|PubMed:11997471, ECO:0000269|PubMed:12089140, ECO:0000269|PubMed:12876288, ECO:0000269|PubMed:12941942}. SufS is one of three members of the NifS protein family in E. coli, the other two being CPLX0-7838 (G7454) and CPLX0-248 (G7325) . The protein was initially thought to function mainly as a pyridoxal 5'-phosphate (PLP)-dependent selenocysteine lyase with high specificity for L-selenocysteine . It was later determined that SufS functions as a PLP-dependent cysteine desulfurase in a secondary pathway of iron-sulfur cluster assembly ; the isc operon encodes the major assembly pathway . The Suf system appears to be responsible for Fe-S cluster synthesis when iron or sulfur metabolism is disrupted by iron starvation or oxidative stress...

## Biological Role

Catalyzes L-cysteine:sulfur-acceptor sulfurtransferase (reaction.R11528). Component of SufS-SufE complex (complex.ecocyc.CPLX0-12491), L-cysteine desulfurase SufS (complex.ecocyc.CPLX0-246).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Cysteine desulfurases mobilize the sulfur from L-cysteine to yield L-alanine, an essential step in sulfur metabolism for biosynthesis of a variety of sulfur-containing biomolecules. Component of the suf operon, which is activated and required under specific conditions such as oxidative stress and iron limitation. Acts as a potent selenocysteine lyase in vitro, that mobilizes selenium from L-selenocysteine. Selenocysteine lyase activity is however unsure in vivo. Can also desulfinate L-cysteine sulfinate (3-sulfino-L-alanine). {ECO:0000269|PubMed:10329673, ECO:0000269|PubMed:10829016, ECO:0000269|PubMed:11997471, ECO:0000269|PubMed:12089140, ECO:0000269|PubMed:12876288, ECO:0000269|PubMed:12941942}.

## Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R11528|reaction.R11528]] `KEGG` `database` - via EC:2.8.1.7
- `is_component_of` --> [[complex.ecocyc.CPLX0-12491|complex.ecocyc.CPLX0-12491]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-246|complex.ecocyc.CPLX0-246]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1680|gene.b1680]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77444`
- `KEGG:ecj:JW1670;eco:b1680;ecoc:C3026_09625;`
- `GeneID:946185;`
- `GO:GO:0001887; GO:0005737; GO:0006534; GO:0006790; GO:0008826; GO:0009000; GO:0016226; GO:0016787; GO:0030170; GO:0031071; GO:0042803`
- `EC:2.8.1.7; 3.13.1.-; 4.4.1.16`

## Notes

Cysteine desulfurase (EC 2.8.1.7) (Cysteine sulfinate desulfinase) (CSD) (EC 3.13.1.-) (Selenocysteine beta-lyase) (SCL) (Selenocysteine lyase) (EC 4.4.1.16) (Selenocysteine reductase)
