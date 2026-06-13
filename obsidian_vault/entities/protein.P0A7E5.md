---
entity_id: "protein.P0A7E5"
entity_type: "protein"
name: "pyrG"
source_database: "UniProt"
source_id: "P0A7E5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:32507415}. Note=Localizes to the cytoophidium, a subcellular filamentary structure where CTP synthase is compartmentalized. Many cells form cytoophidia which are observed in stationary phase. {ECO:0000269|PubMed:32507415}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pyrG b2780 JW2751"
---

# pyrG

`protein.P0A7E5`

## Static

- Type: `protein`
- Source: `UniProt:P0A7E5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:32507415}. Note=Localizes to the cytoophidium, a subcellular filamentary structure where CTP synthase is compartmentalized. Many cells form cytoophidia which are observed in stationary phase. {ECO:0000269|PubMed:32507415}.

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent amination of UTP to CTP with either L-glutamine or ammonia as the source of nitrogen. Regulates intracellular CTP levels through interactions with the four ribonucleotide triphosphates. {ECO:0000269|PubMed:11336655, ECO:0000269|PubMed:8385490, ECO:0000305|PubMed:15157079}.

## Biological Role

Catalyzes L-glutamine amidohydrolase (reaction.R00256), UTP:ammonia ligase (ADP-forming) (reaction.R00571), UTP:L-glutamine amido-ligase (ADP-forming) (reaction.R00573). Component of CTP synthetase (complex.ecocyc.CTPSYN-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent amination of UTP to CTP with either L-glutamine or ammonia as the source of nitrogen. Regulates intracellular CTP levels through interactions with the four ribonucleotide triphosphates. {ECO:0000269|PubMed:11336655, ECO:0000269|PubMed:8385490, ECO:0000305|PubMed:15157079}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00256|reaction.R00256]] `KEGG` `database` - via EC:6.3.4.2
- `catalyzes` --> [[reaction.R00571|reaction.R00571]] `KEGG` `database` - via EC:6.3.4.2
- `catalyzes` --> [[reaction.R00573|reaction.R00573]] `KEGG` `database` - via EC:6.3.4.2
- `is_component_of` --> [[complex.ecocyc.CTPSYN-CPLX|complex.ecocyc.CTPSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2780|gene.b2780]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7E5`
- `KEGG:ecj:JW2751;eco:b2780;ecoc:C3026_15275;`
- `GeneID:93779218;946116;`
- `GO:GO:0000287; GO:0003883; GO:0004359; GO:0005524; GO:0005829; GO:0006241; GO:0019856; GO:0032991; GO:0042802; GO:0044210; GO:0051289; GO:0097268`
- `EC:6.3.4.2`

## Notes

CTP synthase (EC 6.3.4.2) (Cytidine 5'-triphosphate synthase) (Cytidine triphosphate synthetase) (CTP synthetase) (CTPS) (UTP--ammonia ligase)
