---
entity_id: "gene.b1633"
entity_type: "gene"
name: "nth"
source_database: "NCBI RefSeq"
source_id: "gene-b1633"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1633"
  - "nth"
---

# nth

`gene.b1633`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1633`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nth (gene.b1633) is a gene entity. It encodes nth (protein.P0AB83). Encoded protein function: FUNCTION: DNA repair enzyme that has both DNA N-glycosylase activity and AP-lyase activity. The DNA N-glycosylase activity releases various damaged pyrimidines from DNA by cleaving the N-glycosidic bond, leaving an AP (apurinic/apyrimidinic) site. The AP-lyase activity cleaves the phosphodiester bond 3' to the AP site by a beta-elimination, leaving a 3'-terminal unsaturated sugar and a product with a terminal 5'-phosphate. {ECO:0000255|HAMAP-Rule:MF_00942, ECO:0000269|PubMed:2449657, ECO:0000269|PubMed:2669955, ECO:0000269|PubMed:6371006}. EcoCyc product frame: EG10662-MONOMER. Genomic coordinates: 1711523-1712158. EcoCyc protein note: Endonuclease III (Endo III or Nth) is a combined DNA glycosylase and apurinic/apyrimidinic (AP) lyase; Endo III cleaves the N-glycosidic bond of damaged pyrimidines to create AP sites and incises the phosphodiester backbone 3' to the abasic site to yield single strand breaks with 3'-unsaturated aldehydic and deoxyribonucleoside 5'-phosphoryl ends. The AP lyase activity of Endo III generates blocked 3' termini that are then processed by one of two AP endonucleases (EG11073-MONOMER "Exonuclease III" and EG10651-MONOMER "Endonuclease IV") to generate the 3' OH ends that are required for DNA polymerase repair synthesis (see )...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), rpoN (protein.P24255).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB83|protein.P0AB83]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=nth; function=-
- `represses` <-- [[protein.P24255|protein.P24255]] `RegulonDB|EcoCyc` `S` - regulator=RpoN; target=nth; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005463,ECOCYC:EG10662,GeneID:947122`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1711523-1712158:+; feature_type=gene
