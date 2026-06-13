---
entity_id: "protein.P0A7Z4"
entity_type: "protein"
name: "rpoA"
source_database: "UniProt"
source_id: "P0A7Z4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpoA pez phs sez b3295 JW3257"
---

# rpoA

`protein.P0A7Z4`

## Static

- Type: `protein`
- Source: `UniProt:P0A7Z4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: DNA-dependent RNA polymerase (RNAP) catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. This subunit plays an important role in subunit assembly since its dimerization is the first step in the sequential assembly of subunits to form the holoenzyme. {ECO:0000269|PubMed:1646077, ECO:0000269|PubMed:24843001}.; FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNAP. It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis. {ECO:0000269|PubMed:32871103}. RpoA is the α subunit of the RNA polymerase core enzyme. It consists of two domains connected by a flexible linker. The RpoA amino-terminus is both necessary and sufficient for dimerization of RpoA and subsequent assembly of the RNA polymerase core complex . The amino-terminus has been analyzed both by NMR and via a 2.5 Å resolution crystal structure . Protein-Protein Interaction (PPI) networks have been examined with algebraic topology analysis showing that most interacting proteins with RpoA are related to the protein translation...

## Biological Role

Catalyzes ATP:polynucleotide adenylyltransferase; (reaction.R00435), GTP:RNA guanylyltransferase (DNA-directed); (reaction.R00441), CTP:RNA cytidylyltransferase (DNA-directed); (reaction.R00442), UTP:RNA uridylyltransferase (reaction.R00443), nucleoside-triphosphate:RNA nucleotidyltransferase (DNA-directed); (reaction.R00444). Component of RNA polymerase, core enzyme (complex.ecocyc.APORNAP-CPLX), RNA polymerase sigma 19 (complex.ecocyc.CPLX0-221), RNA polymerase sigma 28 (complex.ecocyc.CPLX0-222), RNA polymerase sigma 32 (complex.ecocyc.RNAP32-CPLX), RNA polymerase sigma 54 (complex.ecocyc.RNAP54-CPLX), RNA polymerase sigma 70 (complex.ecocyc.RNAP70-CPLX), RNA polymerase sigma 24 (complex.ecocyc.RNAPE-CPLX), RNA polymerase sigma S (complex.ecocyc.RNAPS-CPLX).

## Enriched Pathways

- `eco03020` RNA polymerase (KEGG)

## Annotation

FUNCTION: DNA-dependent RNA polymerase (RNAP) catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. This subunit plays an important role in subunit assembly since its dimerization is the first step in the sequential assembly of subunits to form the holoenzyme. {ECO:0000269|PubMed:1646077, ECO:0000269|PubMed:24843001}.; FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNAP. It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis. {ECO:0000269|PubMed:32871103}.

## Pathways

- `eco03020` RNA polymerase (KEGG)

## Outgoing Edges (13)

- `catalyzes` --> [[reaction.R00435|reaction.R00435]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` --> [[reaction.R00441|reaction.R00441]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` --> [[reaction.R00442|reaction.R00442]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` --> [[reaction.R00443|reaction.R00443]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` --> [[reaction.R00444|reaction.R00444]] `KEGG` `database` - via EC:2.7.7.6
- `is_component_of` --> [[complex.ecocyc.APORNAP-CPLX|complex.ecocyc.APORNAP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-221|complex.ecocyc.CPLX0-221]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-222|complex.ecocyc.CPLX0-222]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.RNAP32-CPLX|complex.ecocyc.RNAP32-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.RNAP54-CPLX|complex.ecocyc.RNAP54-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.RNAP70-CPLX|complex.ecocyc.RNAP70-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.RNAPE-CPLX|complex.ecocyc.RNAPE-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.RNAPS-CPLX|complex.ecocyc.RNAPS-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3295|gene.b3295]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7Z4`
- `KEGG:ecj:JW3257;eco:b3295;ecoc:C3026_17915;`
- `GeneID:86862307;947794;`
- `GO:GO:0000345; GO:0003677; GO:0003899; GO:0005737; GO:0005829; GO:0006352; GO:0006879; GO:0008023; GO:0009408; GO:0016020; GO:0031564; GO:0032784; GO:0036460; GO:0042128; GO:0044780; GO:0046983; GO:0048870; GO:0071973; GO:0090605; GO:2000142`
- `EC:2.7.7.6`

## Notes

DNA-directed RNA polymerase subunit alpha (RNAP subunit alpha) (EC 2.7.7.6) (RNA polymerase subunit alpha) (Transcriptase subunit alpha)
