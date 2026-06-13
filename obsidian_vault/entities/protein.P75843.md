---
entity_id: "protein.P75843"
entity_type: "protein"
name: "ycaQ"
source_database: "UniProt"
source_id: "P75843"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycaQ b0916 JW0899"
---

# ycaQ

`protein.P75843`

## Static

- Type: `protein`
- Source: `UniProt:P75843`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: DNA glycosylase involved in the repair of interstrand DNA cross-links (ICLs), which are highly toxic DNA lesions that covalently tether the opposing strands of DNA, thereby inhibiting essential cellular processes such as DNA replication and transcription (PubMed:32409837). Acts by unhooking both sides of the ICLs, forming abasic (AP) sites on both strands (PubMed:32409837). Unhooks ICLs derived from various cross-linking agents, including azinomycin B (AZB) and mechlorethamine, also known as nitrogen mustard (NM), protecting cells from the toxicity of these cross-linking agents (PubMed:32409837). In vitro, also acts on monoadducts and can catalyze the excision of N7-methylguanine (7mGua) from an oligonucleotide containing N7-methyldeoxyguanosine (d7mG) (PubMed:32409837). Shows no unhooking activity toward FaPy-ICLs (PubMed:32409837). {ECO:0000269|PubMed:32409837}. YcaQ is an alkylpurine DNA glycosylase which acts on interstrand cross-links (ICLs) formed by alkylation at purine N3 or N7 positions. YcaQ can unhook chemically diverse ICLs, such as those produced by the Streptomyces secondary metabolite, CPD-16517 (CPD-23532 "AZB-ICLs"), and from nitrogen mustard compounds such as CPD-23531 (A-NM5-ICL "NM-ICLs"), in vitro...

## Biological Role

Catalyzes RXN-21728 (reaction.ecocyc.RXN-21728), RXN0-7366 (reaction.ecocyc.RXN0-7366).

## Annotation

FUNCTION: DNA glycosylase involved in the repair of interstrand DNA cross-links (ICLs), which are highly toxic DNA lesions that covalently tether the opposing strands of DNA, thereby inhibiting essential cellular processes such as DNA replication and transcription (PubMed:32409837). Acts by unhooking both sides of the ICLs, forming abasic (AP) sites on both strands (PubMed:32409837). Unhooks ICLs derived from various cross-linking agents, including azinomycin B (AZB) and mechlorethamine, also known as nitrogen mustard (NM), protecting cells from the toxicity of these cross-linking agents (PubMed:32409837). In vitro, also acts on monoadducts and can catalyze the excision of N7-methylguanine (7mGua) from an oligonucleotide containing N7-methyldeoxyguanosine (d7mG) (PubMed:32409837). Shows no unhooking activity toward FaPy-ICLs (PubMed:32409837). {ECO:0000269|PubMed:32409837}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-21728|reaction.ecocyc.RXN-21728]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7366|reaction.ecocyc.RXN0-7366]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0916|gene.b0916]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75843`
- `KEGG:ecj:JW0899;eco:b0916;ecoc:C3026_05640;`
- `GeneID:945524;`
- `GO:GO:0003677; GO:0019104; GO:0036297`
- `EC:3.2.2.-`

## Notes

Interstrand DNA cross-link repair glycosylase (ICL repair glycosylase) (EC 3.2.2.-) (Alkylpurine DNA glycosylase)
