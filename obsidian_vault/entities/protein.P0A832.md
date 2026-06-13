---
entity_id: "protein.P0A832"
entity_type: "protein"
name: "smpB"
source_database: "UniProt"
source_id: "P0A832"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00023, ECO:0000269|PubMed:11917023, ECO:0000269|PubMed:15069072}. Note=The tmRNA-SmpB complex associates with stalled ribosomes (PubMed:10393194, PubMed:11917023, PubMed:15699355, PubMed:20940705, PubMed:22622583). SmpB associates with ribosomes even in the absence of tmRNA (PubMed:15069072). {ECO:0000255|HAMAP-Rule:MF_00023, ECO:0000269|PubMed:10393194, ECO:0000269|PubMed:11917023, ECO:0000269|PubMed:15069072, ECO:0000269|PubMed:15699355, ECO:0000269|PubMed:20940705, ECO:0000269|PubMed:22622583}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "smpB smqB b2620 JW2601"
---

# smpB

`protein.P0A832`

## Static

- Type: `protein`
- Source: `UniProt:P0A832`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00023, ECO:0000269|PubMed:11917023, ECO:0000269|PubMed:15069072}. Note=The tmRNA-SmpB complex associates with stalled ribosomes (PubMed:10393194, PubMed:11917023, PubMed:15699355, PubMed:20940705, PubMed:22622583). SmpB associates with ribosomes even in the absence of tmRNA (PubMed:15069072). {ECO:0000255|HAMAP-Rule:MF_00023, ECO:0000269|PubMed:10393194, ECO:0000269|PubMed:11917023, ECO:0000269|PubMed:15069072, ECO:0000269|PubMed:15699355, ECO:0000269|PubMed:20940705, ECO:0000269|PubMed:22622583}.

## Enriched Summary

FUNCTION: Required for rescue of stalled ribosomes mediated by trans-translation. Binds to tmRNA RNA (also known as SsrA or 10Sa RNA, 363 nucleotides in this organism), required for stable binding of tmRNA to ribosomes (PubMed:10393194, PubMed:11904185, PubMed:11917023). tmRNA and SmpB together mimic tRNA shape, replacing the anticodon stem-loop with SmpB (Probable). tmRNA is encoded by the ssrA gene; the 2 termini fold to resemble tRNA(Ala) and it encodes a 'tag peptide', a short internal open reading frame. Able to recruit charged tmRNA to ribosomes (PubMed:15069072). Does not play a role in transcription, processing or Ala-aminoacylation of tmRNA (PubMed:10393194). Other studies have shown it stimulates aminoacylation of tmRNA (PubMed:11904185, PubMed:11917023). May protect tmRNA from degradation (PubMed:11917023). Binds to tmRNA that cannot be aminoacylated (tmRNA G3A), does not bind to tmRNA mutations near the tRNA-like termini (tmRNA G19C, A334U); other tmRNA mutations that block trans-translation still bind SmpB (PubMed:11917023). With tmRNA may play a role in bacterial persistence (PubMed:23812681). During trans-translation Ala-aminoacylated transfer-messenger RNA acts like a tRNA, entering the A-site of stalled ribosomes, displacing the stalled mRNA...

## Annotation

FUNCTION: Required for rescue of stalled ribosomes mediated by trans-translation. Binds to tmRNA RNA (also known as SsrA or 10Sa RNA, 363 nucleotides in this organism), required for stable binding of tmRNA to ribosomes (PubMed:10393194, PubMed:11904185, PubMed:11917023). tmRNA and SmpB together mimic tRNA shape, replacing the anticodon stem-loop with SmpB (Probable). tmRNA is encoded by the ssrA gene; the 2 termini fold to resemble tRNA(Ala) and it encodes a 'tag peptide', a short internal open reading frame. Able to recruit charged tmRNA to ribosomes (PubMed:15069072). Does not play a role in transcription, processing or Ala-aminoacylation of tmRNA (PubMed:10393194). Other studies have shown it stimulates aminoacylation of tmRNA (PubMed:11904185, PubMed:11917023). May protect tmRNA from degradation (PubMed:11917023). Binds to tmRNA that cannot be aminoacylated (tmRNA G3A), does not bind to tmRNA mutations near the tRNA-like termini (tmRNA G19C, A334U); other tmRNA mutations that block trans-translation still bind SmpB (PubMed:11917023). With tmRNA may play a role in bacterial persistence (PubMed:23812681). During trans-translation Ala-aminoacylated transfer-messenger RNA acts like a tRNA, entering the A-site of stalled ribosomes, displacing the stalled mRNA. The ribosome then switches to translate the ORF on the tmRNA, the nascent peptide is terminated with the 'tag peptide' encoded by the tmRNA and targeted for degradation. The ribosome is freed to recommence translation, which seems to be the essential function of trans-translation. {ECO:0000269|PubMed:10393194, ECO:0000269|PubMed:11904185, ECO:0000269|PubMed:11917023, ECO:0000269|PubMed:15069072, ECO:0000269|PubMed:15699355, ECO:0000269|PubMed:20348441, ECO:0000269|PubMed:20940705, ECO:0000269|PubMed:22622583, ECO:0000269|PubMed:23812681, ECO:0000305|PubMed:20940705}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b2620|gene.b2620]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A832`
- `KEGG:ecj:JW2601;eco:b2620;ecoc:C3026_14500;`
- `GeneID:86860741;93774470;947296;`
- `GO:GO:0003723; GO:0005829; GO:0070929; GO:0070930`

## Notes

SsrA-binding protein (Small protein B)
