---
entity_id: "gene.b2800"
entity_type: "gene"
name: "fucA"
source_database: "NCBI RefSeq"
source_id: "gene-b2800"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2800"
  - "fucA"
---

# fucA

`gene.b2800`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2800`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fucA (gene.b2800) is a gene entity. It encodes fucA (protein.P0AB87). Encoded protein function: FUNCTION: Involved in the degradation of L-fucose and D-arabinose (PubMed:13898172). Catalyzes the reversible cleavage of L-fuculose 1-phosphate (Fuc1P) to yield dihydroxyacetone phosphate (DHAP) and L-lactaldehyde (PubMed:10821675, PubMed:11054289, PubMed:13898172, Ref.8, Ref.9). Also able to catalyze the reversible cleavage of D-ribulose 1-phosphate, but FucA has a higher affinity for L-fuculose 1-phosphate and L-lactaldehyde than for D-ribulose 1-phosphate and glycolaldehyde, respectively (PubMed:4928018). FucA possesses a high specificity for the dihydroxyacetone phosphate (DHAP), but accepts a great variety of different aldehydes and has a strong preference for L-configurated alpha-hydroxy aldehydes (PubMed:10821675, PubMed:13898172, Ref.8). FucA generates a vicinal diol unit having the absolute (3R,4R)-cis configuration (D-erythro) (PubMed:10821675, Ref.8). {ECO:0000269|PubMed:10821675, ECO:0000269|PubMed:11054289, ECO:0000269|PubMed:13898172, ECO:0000269|PubMed:4928018, ECO:0000269|Ref.8, ECO:0000269|Ref.9}. EcoCyc product frame: FUCPALDOL-MONOMER. EcoCyc synonyms: fucC, prd. Genomic coordinates: 2933041-2933688...

## Biological Role

Repressed by hns (protein.P0ACF8), nac (protein.Q47005). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), fucR (protein.P0ACK8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB87|protein.P0AB87]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fucA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=fucA; function=+
- `activates` <-- [[protein.P0ACK8|protein.P0ACK8]] `RegulonDB` `S` - regulator=FucR; target=fucA; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=fucA; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=fucA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009179,ECOCYC:EG10348,GeneID:947282`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2933041-2933688:-; feature_type=gene
