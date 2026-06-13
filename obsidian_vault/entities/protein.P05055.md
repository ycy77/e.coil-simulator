---
entity_id: "protein.P05055"
entity_type: "protein"
name: "pnp"
source_database: "UniProt"
source_id: "P05055"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01595, ECO:0000269|PubMed:16079137}. Note=Has also been isolated in association with the inner membrane."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pnp b3164 JW5851"
---

# pnp

`protein.P05055`

## Static

- Type: `protein`
- Source: `UniProt:P05055`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01595, ECO:0000269|PubMed:16079137}. Note=Has also been isolated in association with the inner membrane.

## Enriched Summary

FUNCTION: Involved in mRNA degradation. Catalyzes the phosphorolysis of single-stranded polyribonucleotides processively in the 3'- to 5'-direction. Also involved, along with RNase II, in tRNA processing. RNases II and R contribute to rRNA degradation during starvation, while RNase R and PNPase are the major contributors to quality control of rRNA during steady state growth (PubMed:21135037). Contributes to degradation of some small RNAs (sRNA) (PubMed:34210798). {ECO:0000255|HAMAP-Rule:MF_01595, ECO:0000269|PubMed:12162954, ECO:0000269|PubMed:18812438, ECO:0000269|PubMed:19327365, ECO:0000269|PubMed:21135037, ECO:0000269|PubMed:34210798, ECO:0000269|PubMed:4866865, ECO:0000269|PubMed:7509797}.

## Biological Role

Catalyzes polyribonucleotide:phosphate adenylyltransferase (reaction.R00437), polyribonucleotide:phosphate uridylyltransferase (reaction.R00438), polyribonucleotide:phosphate guanylyltransferase (reaction.R00439), polyribonucleotide:phosphate cytidylyltransferase (reaction.R00440), polyribonucleotide:phosphate nucleotidyltransferase (reaction.R07282). Component of degradosome (complex.ecocyc.CPLX0-2381), polynucleotide phosphorylase (complex.ecocyc.CPLX0-3521).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: Involved in mRNA degradation. Catalyzes the phosphorolysis of single-stranded polyribonucleotides processively in the 3'- to 5'-direction. Also involved, along with RNase II, in tRNA processing. RNases II and R contribute to rRNA degradation during starvation, while RNase R and PNPase are the major contributors to quality control of rRNA during steady state growth (PubMed:21135037). Contributes to degradation of some small RNAs (sRNA) (PubMed:34210798). {ECO:0000255|HAMAP-Rule:MF_01595, ECO:0000269|PubMed:12162954, ECO:0000269|PubMed:18812438, ECO:0000269|PubMed:19327365, ECO:0000269|PubMed:21135037, ECO:0000269|PubMed:34210798, ECO:0000269|PubMed:4866865, ECO:0000269|PubMed:7509797}.

## Pathways

- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.R00437|reaction.R00437]] `KEGG` `database` - via EC:2.7.7.8
- `catalyzes` --> [[reaction.R00438|reaction.R00438]] `KEGG` `database` - via EC:2.7.7.8
- `catalyzes` --> [[reaction.R00439|reaction.R00439]] `KEGG` `database` - via EC:2.7.7.8
- `catalyzes` --> [[reaction.R00440|reaction.R00440]] `KEGG` `database` - via EC:2.7.7.8
- `catalyzes` --> [[reaction.R07282|reaction.R07282]] `KEGG` `database` - via EC:2.7.7.8
- `is_component_of` --> [[complex.ecocyc.CPLX0-2381|complex.ecocyc.CPLX0-2381]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-3521|complex.ecocyc.CPLX0-3521]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b3164|gene.b3164]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05055`
- `KEGG:ecj:JW5851;eco:b3164;ecoc:C3026_17235;`
- `GeneID:947672;`
- `GO:GO:0000175; GO:0000287; GO:0003723; GO:0004654; GO:0005829; GO:0006396; GO:0006401; GO:0006402; GO:0009408; GO:0016020; GO:0035438; GO:0042802; GO:1990061`
- `EC:2.7.7.8`

## Notes

Polyribonucleotide nucleotidyltransferase (EC 2.7.7.8) (Polynucleotide phosphorylase) (PNPase)
