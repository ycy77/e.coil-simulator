---
entity_id: "protein.P0AES4"
entity_type: "protein"
name: "gyrA"
source_database: "UniProt"
source_id: "P0AES4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01897}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gyrA hisW nalA parD b2231 JW2225"
---

# gyrA

`protein.P0AES4`

## Static

- Type: `protein`
- Source: `UniProt:P0AES4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01897}.

## Enriched Summary

FUNCTION: A type II topoisomerase that negatively supercoils closed circular double-stranded (ds) DNA in an ATP-dependent manner to maintain chromosomes in an underwound state (PubMed:12051842, PubMed:18642932, PubMed:186775, PubMed:19060136, PubMed:19965760, PubMed:20356737, PubMed:22457353, PubMed:23294697, PubMed:3031051, PubMed:7811004, PubMed:9148951). This makes better substrates for topoisomerase IV (ParC and ParE) which is the main enzyme that unlinks newly replicated chromosomes in E.coli (PubMed:9334322). Gyrase catalyzes the interconversion of other topological isomers of dsDNA rings, including catenanes (PubMed:22457352). Relaxes negatively supercoiled DNA in an ATP-independent manner (PubMed:337300). E.coli gyrase has higher supercoiling activity than many other bacterial gyrases; at comparable concentrations E.coli gyrase introduces more supercoils faster than M.tuberculosis gyrase, while M.tuberculosis gyrase has higher decatenation than supercoiling activity compared to E.coli (PubMed:22457352). E.coli makes 15% more negative supercoils in pBR322 plasmid DNA than S.typhimurium; the S.typhimurium GyrB subunit is toxic in E.coli, while the E.coli copy can be expressed in S.typhimurium even though the 2 subunits have 777/804 residues identical (PubMed:17400739). The enzymatic differences between E...

## Biological Role

Component of DNA gyrase (complex.ecocyc.CPLX0-2425).

## Annotation

FUNCTION: A type II topoisomerase that negatively supercoils closed circular double-stranded (ds) DNA in an ATP-dependent manner to maintain chromosomes in an underwound state (PubMed:12051842, PubMed:18642932, PubMed:186775, PubMed:19060136, PubMed:19965760, PubMed:20356737, PubMed:22457353, PubMed:23294697, PubMed:3031051, PubMed:7811004, PubMed:9148951). This makes better substrates for topoisomerase IV (ParC and ParE) which is the main enzyme that unlinks newly replicated chromosomes in E.coli (PubMed:9334322). Gyrase catalyzes the interconversion of other topological isomers of dsDNA rings, including catenanes (PubMed:22457352). Relaxes negatively supercoiled DNA in an ATP-independent manner (PubMed:337300). E.coli gyrase has higher supercoiling activity than many other bacterial gyrases; at comparable concentrations E.coli gyrase introduces more supercoils faster than M.tuberculosis gyrase, while M.tuberculosis gyrase has higher decatenation than supercoiling activity compared to E.coli (PubMed:22457352). E.coli makes 15% more negative supercoils in pBR322 plasmid DNA than S.typhimurium; the S.typhimurium GyrB subunit is toxic in E.coli, while the E.coli copy can be expressed in S.typhimurium even though the 2 subunits have 777/804 residues identical (PubMed:17400739). The enzymatic differences between E.coli gyrase and topoisomerase IV are largely due to the GyrA C-terminal domain (approximately residues 524-841) and specifically the GyrA-box (PubMed:16332690, PubMed:8962066). {ECO:0000269|PubMed:12051842, ECO:0000269|PubMed:16332690, ECO:0000269|PubMed:17400739, ECO:0000269|PubMed:18642932, ECO:0000269|PubMed:186775, ECO:0000269|PubMed:19060136, ECO:0000269|PubMed:19965760, ECO:0000269|PubMed:20356737, ECO:0000269|PubMed:22457352, ECO:0000269|PubMed:22457353, ECO:0000269|PubMed:23294697, ECO:0000269|PubMed:3031051, ECO:0000269|PubMed:337300, ECO:0000269|PubMed:7811004, ECO:0000269|PubMed:8962066, ECO:0000269|PubMed:9148951, ECO:0000269|PubMed:9334322}.; FUNCTION: Negative supercoiling favors strand separation, and DNA replication, transcription, recombination and repair, all of which involve strand separation. Type II topoisomerases break and join 2 DNA strands simultaneously in an ATP-dependent manner.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2425|complex.ecocyc.CPLX0-2425]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2231|gene.b2231]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AES4`
- `KEGG:ecj:JW2225;eco:b2231;ecoc:C3026_12465;`
- `GeneID:75206476;946614;`
- `GO:GO:0003677; GO:0003918; GO:0005524; GO:0005694; GO:0005737; GO:0005829; GO:0006261; GO:0006265; GO:0006351; GO:0008094; GO:0009330; GO:0009410; GO:0016020; GO:0034335; GO:0042802; GO:0046677; GO:2000104`
- `EC:5.6.2.2`

## Notes

DNA gyrase subunit A (EC 5.6.2.2)
