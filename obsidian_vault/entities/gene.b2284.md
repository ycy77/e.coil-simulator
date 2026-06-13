---
entity_id: "gene.b2284"
entity_type: "gene"
name: "nuoF"
source_database: "NCBI RefSeq"
source_id: "gene-b2284"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2284"
  - "nuoF"
---

# nuoF

`gene.b2284`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2284`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nuoF (gene.b2284) is a gene entity. It encodes nuoF (protein.P31979). Encoded protein function: FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. EcoCyc product frame: NUOF-MONOMER. Genomic coordinates: 2400218-2401555. EcoCyc protein note: NuoF is part of the soluble fragment of NADH dehydrogenase I, which represents the electron input part of the enzyme . Based on sequence similarity, NuoF contains the FMN and NADH binding sites . Site-directed mutagenesis of the E95 residue in the predicted NADH binding site led to altered binding of NADH and inhibition by NAD+, and a change in the midpoint potential of the FMN cofactor in Complex I . The E95Q mutation may distort the catalytic site and thereby retard the hydride transfer from NADH to FMN . NADH-dependent production of hydrogen peroxide is increased in the E95Q mutant . NuoF was shown to contain the N3 4Fe-4S cluster; the cysteine residues responsible for ligation of the 4Fe-4S cluster were identified by site-directed mutagenesis . Evolved E...

## Biological Role

Repressed by ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31979|protein.P31979]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nuoF; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nuoF; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nuoF; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nuoF; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=nuoF; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=nuoF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007545,ECOCYC:EG11774,GeneID:946753`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2400218-2401555:-; feature_type=gene
