---
entity_id: "gene.b1479"
entity_type: "gene"
name: "maeA"
source_database: "NCBI RefSeq"
source_id: "gene-b1479"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1479"
  - "maeA"
---

# maeA

`gene.b1479`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1479`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

maeA (gene.b1479) is a gene entity. It encodes maeA (protein.P26616). Encoded protein function: NAD-dependent malic enzyme (NAD-ME) (EC 1.1.1.38) EcoCyc product frame: MALIC-NAD-MONOMER. EcoCyc synonyms: sfcA. Genomic coordinates: 1553972-1555669. EcoCyc protein note: E. coli encodes two "malic enzymes" that catalyze the decarboxylation of malate to form pyruvate with concomitant reduction of NAD(P)+. One enzyme, MaeA (described here) requires NAD+, while the other, MALIC-NADP-MONOMER MaeB, requires NADP+ . Metabolic flux through the malic enzymes during aerobic growth on glycerol as the sole source of carbon appears to be essentially zero . In a strain blocked in the fermentative metabolism of pyruvate, overexpressed NAD+-dependent malate dehydrogenase can support growth by catalyzing the normally non-physiological reductive carboxylation of pyruvate to form malate . MaeA is present as a mixture of monomer, homotetramer and homooctamer in solution . Mg2+ and Mn2+ appear to stabilize two different conformational states of the enzyme . MaeA has been engineered to utilize the bioorthogonal co-substrates nicotinamide flucytosine dinucleotide (NFCD) and nicotinamide cytosine dinucleotide (NCD) in place of NAD . A crystal structure of the engineered variant, L310R/Q401C, has been solved . Expression of maeA is induced by growth on acetate...

## Biological Role

Repressed by fnrS (gene.b4699).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26616|protein.P26616]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[gene.b4699|gene.b4699]] `RegulonDB` `S` - regulator=FnrS; target=maeA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004931,ECOCYC:EG10948,GeneID:946031`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1553972-1555669:-; feature_type=gene
