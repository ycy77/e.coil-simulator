---
entity_id: "gene.b0903"
entity_type: "gene"
name: "pflB"
source_database: "NCBI RefSeq"
source_id: "gene-b0903"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0903"
  - "pflB"
---

# pflB

`gene.b0903`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0903`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pflB (gene.b0903) is a gene entity. It encodes pflB (protein.P09373). Encoded protein function: FUNCTION: Catalyzes the conversion of pyruvate to formate and acetyl-CoA (PubMed:4615902). In addition, may be involved in the control of the activity of the formate channel FocA, via direct interaction with FocA (PubMed:24887098). {ECO:0000269|PubMed:24887098, ECO:0000269|PubMed:4615902}. EcoCyc product frame: PYRUVFORMLY-MONOMER. EcoCyc synonyms: pfl. Genomic coordinates: 951272-953554. EcoCyc protein note: Escherichia coli pyruvate-formate lyase (PflB) is a central enzyme of anaerobic metabolism. It catalyzes the coenzyme A-dependent, non-oxidative cleavage of pyruvate to acetyl-CoA and formate in anaerobically growing cells (see pathway FERMENTATION-PWY). Under anaerobic conditions, induction of transcription of pflB involves CPLX0-7797 and the PHOSPHO-ARCA and ARCB-CPLX regulatory proteins . At the post-translational level the enzyme is regulated by activation . Activation of the inactive enzyme is catalyzed by the same PFLACTENZ-MONOMER that also activates KETOBUTFORMLY-INACT-MONOMER . This activation process requires reduced flavodoxin that is generated via a coenzyme A-acylating PYRUFLAVREDUCT-MONOMER, or FLAVONADPREDUCT-MONOMER . Activation introduces a free radical into the enzyme (see below). PflB utilizes a "ping-pong" mechanism that proceeds via two half-reactions...

## Biological Role

Repressed by yeiE (protein.P0ACR4), narL (protein.P0AF28). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09373|protein.P09373]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pflB; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=pflB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=pflB; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=pflB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003071,ECOCYC:EG10701,GeneID:945514`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:951272-953554:-; feature_type=gene
