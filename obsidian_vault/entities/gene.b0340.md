---
entity_id: "gene.b0340"
entity_type: "gene"
name: "cynS"
source_database: "NCBI RefSeq"
source_id: "gene-b0340"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0340"
  - "cynS"
---

# cynS

`gene.b0340`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0340`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cynS (gene.b0340) is a gene entity. It encodes cynS (protein.P00816). Encoded protein function: FUNCTION: Catalyzes the reaction of cyanate with bicarbonate to produce ammonia and carbon dioxide. EcoCyc product frame: CYANLY-MONOMER. EcoCyc synonyms: cnt, cyaN. Genomic coordinates: 359489-359959. EcoCyc protein note: Cyanase is an inducible enzyme in E. coli and was first reported and subsequently studied in E. coli B . The cyanase operon may have evolved to function in detoxification/decomposition of cyanate arising from intra- and extracellular activities . It was shown that bicarbonate (HCO3-) is a substrate of the enzyme, and that water does not participate as a substrate . The initial product carbamate is unstable and spontaneously decomposes to ammonia and carbon dioxide . The enzyme shows competitive substrate inhibition by both substrates . The native enzyme from E. coli B has a molecular weight of ca. 150 kDa and thus appears to be a homodecamer in solution . A crystal structure of cyanase was solved at 1.65 Å resolution; it showed a homodecamer composed of five dimers. The structure allowed identification of the active site, which is located between dimers and is comprised of residues from four adjacent subunits . The free sulfhydryl group of the single cysteine residue is not required for catalytic activity, but plays a role in stabilizing the decameric structure...

## Biological Role

Activated by rpoD (protein.P00579), cynR (protein.P27111).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00816|protein.P00816]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cynS; function=+
- `activates` <-- [[protein.P27111|protein.P27111]] `RegulonDB` `S` - regulator=CynR; target=cynS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001173,ECOCYC:EG10175,GeneID:948998`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:359489-359959:+; feature_type=gene
