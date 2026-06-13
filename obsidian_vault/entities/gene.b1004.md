---
entity_id: "gene.b1004"
entity_type: "gene"
name: "wrbA"
source_database: "NCBI RefSeq"
source_id: "gene-b1004"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1004"
  - "wrbA"
---

# wrbA

`gene.b1004`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1004`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wrbA (gene.b1004) is a gene entity. It encodes wrbA (protein.P0A8G6). Encoded protein function: FUNCTION: It seems to function in response to environmental stress when various electron transfer chains are affected or when the environment is highly oxidizing. It reduces quinones to the hydroquinone state to prevent interaction of the semiquinone with O2 and production of superoxide. It prefers NADH over NADPH. {ECO:0000269|PubMed:16672604, ECO:0000269|PubMed:9694845}. EcoCyc product frame: PD01343. Genomic coordinates: 1067112-1067708. EcoCyc protein note: The purified WrbA protein has NAD(P)H:quinone oxidoreductase activity . WrbA is related to the flavodoxin family of proteins . Unlike the flavodoxins, WrbA does not have a stabilized semiquinone state. It rapidly takes up two electrons, generating the fully reduced form . Purified WrbA protein binds one FMN per monomer with a binding constant of 2 µM at room temperature, which is weaker than that of typical flavodoxins . Binding of FMN appears to be pH-dependent , and it increases the thermal stability and promotes tetramerization of WrbA . Despite the extensive work on this enzyme, its natural substrate and physiological role remain opaque. A new crystal structure combined with a novel application of quantum mechanical calculations can now constrain computational docking attempts with potential substrates...

## Biological Role

Activated by csgD (protein.P52106), nac (protein.Q47005).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8G6|protein.P0A8G6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=wrbA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=wrbA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003392,ECOCYC:EG11540,GeneID:947263`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1067112-1067708:-; feature_type=gene
