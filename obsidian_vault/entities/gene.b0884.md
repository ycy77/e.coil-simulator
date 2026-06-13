---
entity_id: "gene.b0884"
entity_type: "gene"
name: "infA"
source_database: "NCBI RefSeq"
source_id: "gene-b0884"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0884"
  - "infA"
---

# infA

`gene.b0884`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0884`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

infA (gene.b0884) is a gene entity. It encodes infA (protein.P69222). Encoded protein function: FUNCTION: One of the essential components for the initiation of protein synthesis. Binds in the vicinity of the A-site. Stabilizes the binding of IF-2 and IF-3 on the 30S subunit to which N-formylmethionyl-tRNA(fMet) subsequently binds. Helps modulate mRNA selection, yielding the 30S pre-initiation complex (PIC). Upon addition of the 50S ribosomal subunit, IF-1, IF-2 and IF-3 are released leaving the mature 70S translation initiation complex. {ECO:0000269|PubMed:22562136, ECO:0000269|PubMed:376343}. EcoCyc product frame: EG10504-MONOMER. EcoCyc synonyms: bypA1. Genomic coordinates: 926225-926443. EcoCyc protein note: IF-1 is one of three translation initiation factors in E. coli and is essential for viability . Its functional role has not been fully elucidated; a collection of mutants was generated to attempt to determine the function of IF-1 . It was suggested that the essential function of IF-1 and IF-3 may be to minimize the fraction of ribosomes lacking an initiator tRNA . IF-1 binds to the ribosomal A site , which may suggest a function in translational fidelity; such a function could not be shown . Certain mutations in 16S rRNA disrupt binding of IF-1 to the 30S subunit , and a model where IF-1 modulates specific conformational change during initiation has been suggested...

## Biological Role

Repressed by yeiE (protein.P0ACR4). Activated by rpoD (protein.P00579), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69222|protein.P69222]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=infA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003005,ECOCYC:EG10504,GeneID:945500`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:926225-926443:-; feature_type=gene
