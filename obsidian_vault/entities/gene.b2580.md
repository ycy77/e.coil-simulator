---
entity_id: "gene.b2580"
entity_type: "gene"
name: "ung"
source_database: "NCBI RefSeq"
source_id: "gene-b2580"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2580"
  - "ung"
---

# ung

`gene.b2580`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2580`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ung (gene.b2580) is a gene entity. It encodes ung (protein.P12295). Encoded protein function: FUNCTION: Excises uracil residues from the DNA which can arise as a result of misincorporation of dUMP residues by DNA polymerase or due to deamination of cytosine. EcoCyc product frame: EG11058-MONOMER. Genomic coordinates: 2716754-2717443. EcoCyc protein note: ung encoded uracil-DNA glycosylase (Ung/UDG) is a base-excision repair (BER) glycosylase which catalyses the removal of uracil in both single-stranded and double-stranded DNA (also ); Ung hydrolyses the N-glycosylic bond between uracil and deoxyribose releasing free uracil and leaving an apurinic/apyrimidinic (AP) site in the DNA which is subject to further processing (see ). Ung deficient mutants (ung-1 ) have an increased rate of spontaneous G:C → A:T mutation (also ). Purified Ung excises the pyrimidine analogue and chemotherapy drug, 5-fluorouracil, from DNA ; purified Ung excises 5-hydroxyuracil from DNA ; purified Ung excises isodialuric acid - a major cytosine oxidation product - from DNA . Ung activity is inhibited after phage T5 infection (and see ); Ung is inhibited by the Bacillus subtilis phage PBS-1 and PBS-2 encoded inhibitor protein, Ugi...

## Biological Role

Repressed by cpxR (protein.P0AE88). Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P12295|protein.P12295]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=ung; function=+
- `represses` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=ung; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008495,ECOCYC:EG11058,GeneID:947067`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2716754-2717443:+; feature_type=gene
