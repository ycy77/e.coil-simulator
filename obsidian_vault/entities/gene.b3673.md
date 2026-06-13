---
entity_id: "gene.b3673"
entity_type: "gene"
name: "emrD"
source_database: "NCBI RefSeq"
source_id: "gene-b3673"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3673"
  - "emrD"
---

# emrD

`gene.b3673`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3673`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

emrD (gene.b3673) is a gene entity. It encodes emrD (protein.P31442). Encoded protein function: FUNCTION: Multidrug resistance pump that participates in a low energy shock adaptive response. EcoCyc product frame: EMRD-MONOMER. EcoCyc synonyms: yicQ. Genomic coordinates: 3853922-3855106. EcoCyc protein note: EmrD is implicated in the adaptive response to uncouplers of oxidative phosphorylation: disruption of emrD via transposon mutagenesis results in increased sensitivity to carbonyl cyanide m-chlorophenylhydrazone (CCCP) and tetrachlorosalicylanilide (TSA) compared to wild type; emrD expression is induced by uncouplers and is subject to catabolite repression . emrD encodes a putative 12 α-helix transmembrane translocase . Multicopy expression of emrD in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ), confers increased resistance to SDS and benzalkonium but does not impact the resistance to a range of other antibiotics and toxic compounds including CCCP . Purified EmrD binds Hoechst33342 and doxorubicin with micromolar affinity; EmrD transports Hoechst weakly and expression of emrD in a drug-sensitive background (ΔacrAB ΔemrE ΔmdfA) does not confer increased resistance to benzalkonium chloride, CCCP, doxorubicin or Hoechst3334 . In the 3...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31442|protein.P31442]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012011,ECOCYC:EG11693,GeneID:948180`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3853922-3855106:+; feature_type=gene
