---
entity_id: "gene.b2704"
entity_type: "gene"
name: "srlB"
source_database: "NCBI RefSeq"
source_id: "gene-b2704"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2704"
  - "srlB"
---

# srlB

`gene.b2704`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2704`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

srlB (gene.b2704) is a gene entity. It encodes srlB (protein.P05706). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II complex composed of SrlA, SrlB and SrlE is involved in glucitol/sorbitol transport. It can also use D-mannitol. {ECO:0000269|PubMed:1100608}. EcoCyc product frame: GUTB-MONOMER. EcoCyc synonyms: gutB. Genomic coordinates: 2827362-2827733. EcoCyc protein note: Contains a PTS Enzyme IIA (formerly Enzyme III) domain. The hydropathic profile of SrlB is typical of a soluble protein. SrlB may possess a net negative charge at neutral pH as predicted from it's amino acid sequence . srlB, among other genes involved in carbon source transport and metabolism, was downregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05706|protein.P05706]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=srlB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008894,ECOCYC:EG10970,GeneID:948971`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2827362-2827733:+; feature_type=gene
