---
entity_id: "protein.P03960"
entity_type: "protein"
name: "kdpB"
source_database: "UniProt"
source_id: "P03960"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00285, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00285, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kdpB b0697 JW0685"
---

# kdpB

`protein.P03960`

## Static

- Type: `protein`
- Source: `UniProt:P03960`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00285, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00285, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:28636601, ECO:0000269|PubMed:30478378}.

## Enriched Summary

FUNCTION: Part of the high-affinity ATP-driven potassium transport (or Kdp) system, which catalyzes the hydrolysis of ATP coupled with the electrogenic transport of potassium into the cytoplasm (PubMed:23930894, PubMed:2849541, PubMed:8499455). This subunit is responsible for energy coupling to the transport system and for the release of the potassium ions to the cytoplasm (PubMed:16354672, PubMed:30478378, PubMed:34272288). {ECO:0000269|PubMed:16354672, ECO:0000269|PubMed:23930894, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:30478378, ECO:0000269|PubMed:34272288, ECO:0000269|PubMed:8499455}. KdpB is the largest subunit of a potassium ion importing P-type ATPase; KdpB forms a phosphorylated intermediate as part of the transport cycle . KdpB contains seven transmembrane (TM) helices and two large cytoplasmic domains; the first of these is located between TM 2 and 3 and is known as the actuator- or A-domain; the second is located between TM 4 and 5 and consists of a phosphorylation- or P-domain and a nucleotide-binding- or N-domain (see and ). Asp-307, within the conserved DKTGT motif in the P-domain is the site of transient phosphorylation . Two conserved charged residues, D583 and K586, located within TM 5, establish a dipole which has been implicated in energy coupling between the KdpB and KdpA subunits...

## Biological Role

Component of K+ transporting P-type ATPase (complex.ecocyc.ATPASE-1-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the high-affinity ATP-driven potassium transport (or Kdp) system, which catalyzes the hydrolysis of ATP coupled with the electrogenic transport of potassium into the cytoplasm (PubMed:23930894, PubMed:2849541, PubMed:8499455). This subunit is responsible for energy coupling to the transport system and for the release of the potassium ions to the cytoplasm (PubMed:16354672, PubMed:30478378, PubMed:34272288). {ECO:0000269|PubMed:16354672, ECO:0000269|PubMed:23930894, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:30478378, ECO:0000269|PubMed:34272288, ECO:0000269|PubMed:8499455}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ATPASE-1-CPLX|complex.ecocyc.ATPASE-1-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0697|gene.b0697]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P03960`
- `KEGG:ecj:JW0685;eco:b0697;ecoc:C3026_03480;`
- `GeneID:947450;`
- `GO:GO:0000287; GO:0005524; GO:0005886; GO:0006813; GO:0008556; GO:0016887; GO:0031004; GO:0071805; GO:0098655; GO:1903103`
- `EC:7.2.2.6`

## Notes

Potassium-transporting ATPase ATP-binding subunit (EC 7.2.2.6) (ATP phosphohydrolase [potassium-transporting] B chain) (Potassium-binding and translocating subunit B) (Potassium-translocating ATPase B chain)
