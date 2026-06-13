---
entity_id: "protein.P0AD89"
entity_type: "protein"
name: "tnaC"
source_database: "UniProt"
source_id: "P0AD89"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tnaC tnaL b3707 JW3685"
---

# tnaC

`protein.P0AD89`

## Static

- Type: `protein`
- Source: `UniProt:P0AD89`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Required for tryptophan-regulated expression of the tna operon. In the presence of high levels of L-Trp release of this nascent peptide by release factor 2 (RF2, prfB) is inhibited. The ribosome stalls with Pro-24 in the P site and a UGA stop codon in the A site. This prevents transcription termination factor Rho binding, and thus allows transcription and translation of downstream TnaA and TnaB (PubMed:12228716, PubMed:34504068). The presence of TnaC and L-Trp prevents the catalytic GGQ motif of RF2 from engaging with the peptidyl-transferase center (PTC); nucleotides of the PTC are perturbed while Arg-23 probably clashes with 'N5-methyl-Gln-252' of RF2, preventing RF2 from reaching the PTC, and from releasing the translated TnaC peptide (PubMed:34403461, PubMed:34504068). Translation of this peptide turns the ribosome into a small-molecule sensor specifically recognizing L-Trp (PubMed:34403461, PubMed:34504068). {ECO:0000269|PubMed:12228716, ECO:0000269|PubMed:34403461, ECO:0000269|PubMed:34504068}. The TnaC leader peptide is required for regulation by attenuation of the TU00085 operon. The tnaCAB operon codes for two key enzymes in tryptophan metabolism, including tryptophanase. It is regulated by attenuation within its leader region in response to tryptophan abundance...

## Annotation

FUNCTION: Required for tryptophan-regulated expression of the tna operon. In the presence of high levels of L-Trp release of this nascent peptide by release factor 2 (RF2, prfB) is inhibited. The ribosome stalls with Pro-24 in the P site and a UGA stop codon in the A site. This prevents transcription termination factor Rho binding, and thus allows transcription and translation of downstream TnaA and TnaB (PubMed:12228716, PubMed:34504068). The presence of TnaC and L-Trp prevents the catalytic GGQ motif of RF2 from engaging with the peptidyl-transferase center (PTC); nucleotides of the PTC are perturbed while Arg-23 probably clashes with 'N5-methyl-Gln-252' of RF2, preventing RF2 from reaching the PTC, and from releasing the translated TnaC peptide (PubMed:34403461, PubMed:34504068). Translation of this peptide turns the ribosome into a small-molecule sensor specifically recognizing L-Trp (PubMed:34403461, PubMed:34504068). {ECO:0000269|PubMed:12228716, ECO:0000269|PubMed:34403461, ECO:0000269|PubMed:34504068}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3707|gene.b3707]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD89`
- `KEGG:ecj:JW3685;eco:b3707;ecoc:C3026_20100;`
- `GeneID:89518606;948223;`
- `GO:GO:0006569; GO:0019843; GO:0031556; GO:0090358`

## Notes

Tryptophanase operon leader peptide (TnaC)
