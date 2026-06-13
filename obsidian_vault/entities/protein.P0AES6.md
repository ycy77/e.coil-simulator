---
entity_id: "protein.P0AES6"
entity_type: "protein"
name: "gyrB"
source_database: "UniProt"
source_id: "P0AES6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01898}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gyrB acrB cou himB hisU nalC parA pcbA b3699 JW5625"
---

# gyrB

`protein.P0AES6`

## Static

- Type: `protein`
- Source: `UniProt:P0AES6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01898}.

## Enriched Summary

FUNCTION: DNA gyrase negatively supercoils closed circular double-stranded DNA in an ATP-dependent manner to maintain chromosomes in an underwound state (PubMed:12051842, PubMed:12051843, PubMed:1323022, PubMed:18642932, PubMed:186775, PubMed:19060136, PubMed:19965760, PubMed:20356737, PubMed:20675723, PubMed:22457353, PubMed:23294697, PubMed:23352267, PubMed:24386374, PubMed:25202966, PubMed:25849408, PubMed:3031051, PubMed:7811004, PubMed:8248233, PubMed:8621650, PubMed:9657678). This makes better substrates for topoisomerase 4 (ParC and ParE) which is the main enzyme that unlinks newly replicated chromosomes in E.coli (PubMed:9334322). Gyrase catalyzes the interconversion of other topological isomers of double-stranded DNA rings, including catenanes (PubMed:22457352). Relaxes negatively supercoiled DNA in an ATP-independent manner (PubMed:337300). E.coli gyrase has higher supercoiling activity than other characterized bacterial gyrases; at comparable concentrations E.coli gyrase introduces more supercoils faster than M.tuberculosis gyrase, while M.tuberculosis gyrase has higher decatenation than supercoiling activity compared to E.coli (PubMed:22457352). E.coli makes 15% more negative supercoils in pBR322 plasmid DNA than S.typhimurium; the S.typhimurium GyrB subunit is toxic in E.coli, while the E.coli copy can be expressed in S...

## Biological Role

Component of DNA gyrase (complex.ecocyc.CPLX0-2425).

## Annotation

FUNCTION: DNA gyrase negatively supercoils closed circular double-stranded DNA in an ATP-dependent manner to maintain chromosomes in an underwound state (PubMed:12051842, PubMed:12051843, PubMed:1323022, PubMed:18642932, PubMed:186775, PubMed:19060136, PubMed:19965760, PubMed:20356737, PubMed:20675723, PubMed:22457353, PubMed:23294697, PubMed:23352267, PubMed:24386374, PubMed:25202966, PubMed:25849408, PubMed:3031051, PubMed:7811004, PubMed:8248233, PubMed:8621650, PubMed:9657678). This makes better substrates for topoisomerase 4 (ParC and ParE) which is the main enzyme that unlinks newly replicated chromosomes in E.coli (PubMed:9334322). Gyrase catalyzes the interconversion of other topological isomers of double-stranded DNA rings, including catenanes (PubMed:22457352). Relaxes negatively supercoiled DNA in an ATP-independent manner (PubMed:337300). E.coli gyrase has higher supercoiling activity than other characterized bacterial gyrases; at comparable concentrations E.coli gyrase introduces more supercoils faster than M.tuberculosis gyrase, while M.tuberculosis gyrase has higher decatenation than supercoiling activity compared to E.coli (PubMed:22457352). E.coli makes 15% more negative supercoils in pBR322 plasmid DNA than S.typhimurium; the S.typhimurium GyrB subunit is toxic in E.coli, while the E.coli copy can be expressed in S.typhimurium even though the 2 subunits have 777/804 residues identical (PubMed:17400739). The enzymatic differences between E.coli gyrase and topoisomerase IV are largely due to the GyrA C-terminal domain (approximately residues 524-841) and specifically the GyrA-box (PubMed:16332690, PubMed:8962066). {ECO:0000269|PubMed:12051842, ECO:0000269|PubMed:12051843, ECO:0000269|PubMed:1323022, ECO:0000269|PubMed:16332690, ECO:0000269|PubMed:17400739, ECO:0000269|PubMed:18642932, ECO:0000269|PubMed:186775, ECO:0000269|PubMed:19060136, ECO:0000269|PubMed:19965760, ECO:0000269|PubMed:20356737, ECO:0000269|PubMed:20675723, ECO:0000269|PubMed:22457352, ECO:0000269|PubMed:22457353, ECO:0000269|PubMed:23294697, ECO:0000269|PubMed:23352267, ECO:0000269|PubMed:24386374, ECO:0000269|PubMed:25202966, ECO:0000269|PubMed:25849408, ECO:0000269|PubMed:3031051, ECO:0000269|PubMed:337300, ECO:0000269|PubMed:7811004, ECO:0000269|PubMed:8248233, ECO:0000269|PubMed:8621650, ECO:0000269|PubMed:8962066, ECO:0000269|PubMed:9148951, ECO:0000269|PubMed:9334322, ECO:0000269|PubMed:9657678}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2425|complex.ecocyc.CPLX0-2425]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3699|gene.b3699]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AES6`
- `KEGG:ecj:JW5625;eco:b3699;ecoc:C3026_20055;`
- `GeneID:93778440;948211;`
- `GO:GO:0003677; GO:0003918; GO:0005524; GO:0005694; GO:0005737; GO:0005829; GO:0006261; GO:0006265; GO:0006351; GO:0008094; GO:0009330; GO:0009410; GO:0034335; GO:0046677; GO:0046872`
- `EC:5.6.2.2`

## Notes

DNA gyrase subunit B (EC 5.6.2.2) (Type IIA topoisomerase subunit GyrB)
