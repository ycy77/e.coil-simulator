---
entity_id: "gene.b0587"
entity_type: "gene"
name: "fepE"
source_database: "NCBI RefSeq"
source_id: "gene-b0587"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0587"
  - "fepE"
---

# fepE

`gene.b0587`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0587`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fepE (gene.b0587) is a gene entity. It encodes fepE (protein.P26266). Encoded protein function: FUNCTION: Part of the ferric enterobactin transport system. EcoCyc product frame: EG10297-MONOMER. Genomic coordinates: 618254-619387. EcoCyc protein note: The fepE locus was originally defined by an enterobactin transport lesion; a fepE::mini-kan-9 strain is able to produce enterobactin but is unable to grow in either iron-depleted medium or with addition of purified enterobactin . A fepE homolog in TAX-90371 is responsible for very long O antigen polymerization in lipopolysaccharide, providing minor complement resistance and significant serum resistance in mouse infection models , and is upregulated during swarming . fepE is regulated by the FlhDC flagellar transcriptional regulator .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), nac (protein.Q47005). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26266|protein.P26266]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fepE; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=fepE; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fepE; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=fepE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002023,ECOCYC:EG10297,GeneID:945180`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:618254-619387:+; feature_type=gene
