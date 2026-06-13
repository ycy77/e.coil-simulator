---
entity_id: "gene.b2866"
entity_type: "gene"
name: "xdhA"
source_database: "NCBI RefSeq"
source_id: "gene-b2866"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2866"
  - "xdhA"
---

# xdhA

`gene.b2866`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2866`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xdhA (gene.b2866) is a gene entity. It encodes xdhA (protein.Q46799). Encoded protein function: FUNCTION: Presumed to be a dehydrogenase, but possibly an oxidase. Participates in limited purine salvage (requires aspartate) but does not support aerobic growth on purines as the sole carbon source (purine catabolism). Deletion results in increased adenine sensitivity, suggesting that this protein contributes to the conversion of adenine to guanine nucleotides during purine salvage. {ECO:0000269|PubMed:10986234}. EcoCyc product frame: G7485-MONOMER. EcoCyc synonyms: ygeS. Genomic coordinates: 3000345-3002603. EcoCyc protein note: XdhA has similarity to the molybdenum cofactor-containing domains of Drosophila melanogaster xanthine dehydrogenase and Desulfovibrio gigas aldehyde oxidoreductase . An xdhA mutant exhibits a defect in an indirect assay of xanthine dehydrogenase activity and exhibits sensitivity to adenine, which is indicative of a defect in purine salvage . The mutant exhibits more rapid growth than wild type utilizing aspartate as the source of nitrogen and growth under these conditions is stimulated by hypoxanthine . The mutant shows wild-type growth utilizing abundant ammonia as the nitrogen source .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoN (protein.P24255).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46799|protein.Q46799]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=xdhA; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=xdhA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009413,ECOCYC:G7485,GeneID:947116`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3000345-3002603:+; feature_type=gene
