---
entity_id: "gene.b2286"
entity_type: "gene"
name: "nuoC"
source_database: "NCBI RefSeq"
source_id: "gene-b2286"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2286"
  - "nuoC"
---

# nuoC

`gene.b2286`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2286`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nuoC (gene.b2286) is a gene entity. It encodes nuoC (protein.P33599). Encoded protein function: FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. EcoCyc product frame: NUOC-MONOMER. EcoCyc synonyms: nuoD. Genomic coordinates: 2402055-2403845. EcoCyc protein note: NuoCD is part of the connecting fragment within the peripheral arm of NADH:ubiquinone oxidoreductase I (NDH-1). Unlike in other bacteria, which contain two separate genes encoding the NuoC and NuoD subunits, the nuoC gene of E. coli K-12 encodes a fused version of these subunits . NuoCD is the only subunit of the peripheral arm that does not contain a cofactor. This subunit was predicted to function as the proton channel . NuoCD interacts with FliG and FliM, components of the flagellar switch-motor complex . Mutagenesis of two conserved histidine residues, H224 and H228, only has a modest effect on ubiquinone reductase activity of NDH-1...

## Biological Role

Repressed by ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33599|protein.P33599]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nuoC; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nuoC; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nuoC; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nuoC; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=nuoC; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=nuoC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007549,ECOCYC:EG12084,GeneID:946759`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2402055-2403845:-; feature_type=gene
