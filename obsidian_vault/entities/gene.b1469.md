---
entity_id: "gene.b1469"
entity_type: "gene"
name: "narU"
source_database: "NCBI RefSeq"
source_id: "gene-b1469"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1469"
  - "narU"
---

# narU

`gene.b1469`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1469`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narU (gene.b1469) is a gene entity. It encodes narU (protein.P37758). Encoded protein function: FUNCTION: Catalyzes nitrate uptake, nitrite uptake and nitrite export across the cytoplasmic membrane. May function as a nitrate/H(+) and nitrite/H(+) channel. Could confer a selective advantage during severe nutrient starvation or slow growth. {ECO:0000269|PubMed:11967075, ECO:0000269|PubMed:15667293, ECO:0000269|PubMed:16804183, ECO:0000269|PubMed:18691156}. EcoCyc product frame: NARU-MONOMER. EcoCyc synonyms: yddF. Genomic coordinates: 1542672-1544060. EcoCyc protein note: NarU catalyses nitrate uptake and nitrite export by an unknown mechanism in. NarU is a member of the major facilitator superfamily (MFS) of transporters , and is highly similar to the nitrate:nitrite antiporter NARK-MONOMER "NarK" . narU forms an operon with narZYWV, encoding NITRATREDUCTZ-CPLX . An RPOS-MONOMER "RpoS"-dependent promoter is located upstream of the narU transcription start site . narU expressed from a plasmid restores the ability of a strain lacking narK to export nitrite from the cytoplasm . Δ(narUnarK) strains are defective in nitrate dependent growth; single ΔnarU or ΔnarK strains can import nitrate at rates similar to wild-type. A multicopy plasmid expressing narU complements a narK mutation for nitrite excretion but not uptake...

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), ompR (protein.P0AA16).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37758|protein.P37758]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=narU; function=+
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=narU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004901,ECOCYC:EG12153,GeneID:945799`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1542672-1544060:-; feature_type=gene
