---
entity_id: "protein.P76273"
entity_type: "protein"
name: "rsmF"
source_database: "UniProt"
source_id: "P76273"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsmF yebU b1835 JW5301"
---

# rsmF

`protein.P76273`

## Static

- Type: `protein`
- Source: `UniProt:P76273`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically methylates the cytosine at position 1407 (m5C1407) of 16S rRNA (PubMed:16678201). In vitro, methylates the assembled 30S subunit, but not naked 16S rRNA or the 70S ribosome (PubMed:16678201). {ECO:0000269|PubMed:16678201}.; FUNCTION: In addition, during cellular stress, methylates the cytosine at position 49 (m5C49) of the tyrosine transfer RNA (tRNA Tyr-QUA-II). {ECO:0000269|PubMed:39495928}. RsmF is a dual-substrate RNA-modifying methyltransferase responsible for methylation of 16S rRNA at the C5 position of the C1407 nucleotide and for m5c modification to the anticodon of TYR-tRNAs tRNATyr at position C49 . In vitro, the enzyme methylates 16S rRNA within the 30S ribosomal subunit, but not naked 16S rRNA or 70S ribosomes . The enzyme was identified by similarity to the RsmB methyltransferase, which is responsible for methylation of C967 of 16S rRNA . A crystal structure of RsmF has been solved at 2.9 Å resolution. The enzyme has an N-terminal catalytic domain that binds S-adenosylmethionine; the C-terminal domain has structural similarity to PUA domains of pseudouridine synthases and archaeosine-specific transglycosylases. A mechanism for substrate specificity and recognition has been proposed . Methylation of G1405 by the aminoglycoside resistance methyltransferases Sgm , ArmA, RmtB, and RmtC interferes with methylation of C1407 by RsmF...

## Biological Role

Catalyzes RXN-11593 (reaction.ecocyc.RXN-11593).

## Annotation

FUNCTION: Specifically methylates the cytosine at position 1407 (m5C1407) of 16S rRNA (PubMed:16678201). In vitro, methylates the assembled 30S subunit, but not naked 16S rRNA or the 70S ribosome (PubMed:16678201). {ECO:0000269|PubMed:16678201}.; FUNCTION: In addition, during cellular stress, methylates the cytosine at position 49 (m5C49) of the tyrosine transfer RNA (tRNA Tyr-QUA-II). {ECO:0000269|PubMed:39495928}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11593|reaction.ecocyc.RXN-11593]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1835|gene.b1835]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76273`
- `KEGG:ecj:JW5301;eco:b1835;ecoc:C3026_10455;`
- `GeneID:946348;`
- `GO:GO:0003723; GO:0005737; GO:0009383; GO:0070475`
- `EC:2.1.1.-; 2.1.1.178`

## Notes

Ribosomal RNA small subunit methyltransferase F (EC 2.1.1.178) (16S rRNA m5C1407 methyltransferase) (rRNA (cytosine-C(5)-)-methyltransferase RsmF) (rRNA small subunit methyltransferase RsmF) (tRNA (cytosine(49)-C(5))-methyltransferase) (EC 2.1.1.-)
