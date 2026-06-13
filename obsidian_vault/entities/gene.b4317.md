---
entity_id: "gene.b4317"
entity_type: "gene"
name: "fimD"
source_database: "NCBI RefSeq"
source_id: "gene-b4317"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4317"
  - "fimD"
---

# fimD

`gene.b4317`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4317`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fimD (gene.b4317) is a gene entity. It encodes fimD (protein.P30130). Encoded protein function: FUNCTION: Involved in the export and assembly of FimA fimbrial subunits across the outer membrane. EcoCyc product frame: EG10311-MONOMER. EcoCyc synonyms: fimD_1, fimD_2. Genomic coordinates: 4545096-4547732. EcoCyc protein note: FimD is a member of the Fimbrial Usher Porin (FUP) family . FimD is the usher constituent in the type 1 pilus (fimbrial) chaperone-usher pathway in Escherichia coli. During CPLX0-3401 "type 1 pilus" assembly, the chaperone-subunit complex composed of the FimC chaperone and the FimA, FimF, FimG or FimH subunit is targeted to the FimD usher which facilitates assembly of the pilus and subsequent translocation across the outer membrane . Type 1 pili mediate recognition of and adhesion to, host tissues and much of our knowledge regarding type 1 pili in E. coli is derived from studies using uropathogenic strains. FimD consists of 5 functional domains: an N-terminal domain (NTD), a pore domain that, in the resting state, is occluded by a plug domain and two carboxy-terminal domains (CTD1 and CTD2) . The purified N-terminal 139 residues of FimD binds FimC-FimH and FimC-FimF complexes in vitro . Cryo-electron microscopy of FimD bound to translocating FimC:F:G:H suggests that the functional usher forms twinned translocation channels...

## Biological Role

Activated by rpoD (protein.P00579), fis (protein.P0A6R3), hns (protein.P0ACF8), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30130|protein.P30130]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fimD; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=fimD; function=+
- `activates` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=fimD; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=fimD; function=+

## External IDs

- `Dbxref:ECOCYC:EG10311,GeneID:948844`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4545096-4547732:+; feature_type=gene
