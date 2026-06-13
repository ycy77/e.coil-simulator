---
entity_id: "gene.b2297"
entity_type: "gene"
name: "pta"
source_database: "NCBI RefSeq"
source_id: "gene-b2297"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2297"
  - "pta"
---

# pta

`gene.b2297`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2297`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pta (gene.b2297) is a gene entity. It encodes pta (protein.P0A9M8). Encoded protein function: FUNCTION: Involved in acetate metabolism (PubMed:16080684). Catalyzes the reversible interconversion of acetyl-CoA and acetyl phosphate (PubMed:16080684). The direction of the overall reaction changes depending on growth conditions (PubMed:16080684). On minimal medium acetyl-CoA is generated. In rich medium acetyl-CoA is converted to acetate and allowing the cell to dump the excess of acetylation potential in exchange for energy in the form of ATP (PubMed:15687190). The main pathway for acetate production during exponential phase (PubMed:16080684). {ECO:0000269|PubMed:15687190, ECO:0000269|PubMed:16080684}. EcoCyc product frame: PHOSACETYLTRANS-MONOMER. Genomic coordinates: 2414747-2416891. EcoCyc protein note: Phosphate acetyltransferase (Pta) catalyzes the reversible conversion between acetyl-CoA and acetylphosphate, a step in the metabolism of acetate. Both pyruvate and phosphoenolpyruvate activate the enzyme in the direction of acetylphosphate synthesis and inhibit the enzyme in the direction of acetyl-CoA synthesis . Pta is composed of three domains; only the C-terminal domain is required for phosphate acetyltransferase activity. The N-terminal domain is involved in stabilization of the native quarternary structure and metabolic regulation...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9M8|protein.P0A9M8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pta; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007582,ECOCYC:EG20173,GeneID:946778`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2414747-2416891:+; feature_type=gene
