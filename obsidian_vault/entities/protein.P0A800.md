---
entity_id: "protein.P0A800"
entity_type: "protein"
name: "rpoZ"
source_database: "UniProt"
source_id: "P0A800"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpoZ b3649 JW3624"
---

# rpoZ

`protein.P0A800`

## Static

- Type: `protein`
- Source: `UniProt:P0A800`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Promotes RNA polymerase (RNAP) assembly. Latches the N- and C-terminal regions of the beta' subunit thereby facilitating its interaction with the beta and alpha subunits. {ECO:0000269|PubMed:24843001}.; FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNAP. It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis. {ECO:0000269|PubMed:32871103}. RpoZ copurifies with RNA polymerase and may play a structural role in that complex. RpoZ copurifies with APORNAP-CPLX and, when added during renaturation studies, maximizes the yield of functional polymerase . RpoZ binds to RPOC-MONOMER, preventing its aggregation during renaturation and assisting in its addition to the partially formed polymerase complex . The initiating methionine of RpoZ is cleaved . Recombinant RpoZ is also cleaved by an endogenous protease, most likely by EG10673-MONOMER . Under exponential growth conditions with an rpoZ mutant, σ38 transcription is enhanced in parallel with overall DNA relaxation. Overproduction of σ70 in an rpoZ mutant increased both overall DNA supercoiling and the transcription of genes utilizing high levels of negative superhelicity...

## Biological Role

Catalyzes ATP:polynucleotide adenylyltransferase; (reaction.R00435), GTP:RNA guanylyltransferase (DNA-directed); (reaction.R00441), CTP:RNA cytidylyltransferase (DNA-directed); (reaction.R00442), UTP:RNA uridylyltransferase (reaction.R00443), nucleoside-triphosphate:RNA nucleotidyltransferase (DNA-directed); (reaction.R00444).

## Enriched Pathways

- `eco03020` RNA polymerase (KEGG)

## Annotation

FUNCTION: Promotes RNA polymerase (RNAP) assembly. Latches the N- and C-terminal regions of the beta' subunit thereby facilitating its interaction with the beta and alpha subunits. {ECO:0000269|PubMed:24843001}.; FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNAP. It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis. {ECO:0000269|PubMed:32871103}.

## Pathways

- `eco03020` RNA polymerase (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00435|reaction.R00435]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` --> [[reaction.R00441|reaction.R00441]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` --> [[reaction.R00442|reaction.R00442]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` --> [[reaction.R00443|reaction.R00443]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` --> [[reaction.R00444|reaction.R00444]] `KEGG` `database` - via EC:2.7.7.6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3649|gene.b3649]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A800`
- `KEGG:ecj:JW3624;eco:b3649;ecoc:C3026_19770;`
- `GeneID:948160;99703809;99809591;`
- `GO:GO:0000345; GO:0001000; GO:0003677; GO:0003899; GO:0005829; GO:0006352; GO:0006879; GO:0008023; GO:0009408; GO:0030880; GO:0031564; GO:0032784; GO:0036460; GO:0042128; GO:0044780; GO:0048870; GO:0065003; GO:0071973; GO:0090605; GO:2000142`
- `EC:2.7.7.6`

## Notes

DNA-directed RNA polymerase subunit omega (RNAP omega subunit) (EC 2.7.7.6) (RNA polymerase omega subunit) (Transcriptase subunit omega)
