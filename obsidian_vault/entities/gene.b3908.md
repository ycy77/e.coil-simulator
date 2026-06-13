---
entity_id: "gene.b3908"
entity_type: "gene"
name: "sodA"
source_database: "NCBI RefSeq"
source_id: "gene-b3908"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3908"
  - "sodA"
---

# sodA

`gene.b3908`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3908`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sodA (gene.b3908) is a gene entity. It encodes sodA (protein.P00448). Encoded protein function: FUNCTION: Destroys superoxide anion radicals which are normally produced within the cells and which are toxic to biological systems. EcoCyc product frame: SUPEROX-DISMUTMN-MONOMER. Genomic coordinates: 4100810-4101430. EcoCyc protein note: SodA, or MnSOD, is one of three superoxide dismutases in E. coli . The three enzymes differ in their metal cofactor requirement; MnSOD contains manganese. Superoxide dismutase is implicated in the response to a large number of environmental changes that lead to the generation of superoxide radicals. MnSOD and the iron-containing enzyme SUPEROX-DISMUTFE-MONOMER FeSOD (SodB) are not functionally equivalent; MnSOD is more effective than FeSOD in preventing damage to DNA, while FeSOD seems more effective in protecting a cytoplasmic superoxide-sensitive enzyme . However, both enzymes were shown to protect dihydroxy acid dehydratase from inactivation by oxidative stress . MnSOD binds DNA non-specifically with a Ka of 3 x 105 M-1 . The superoxide dismutases contribute to reducing iron toxicity . The enzyme is highly specific for the manganese cofactor; an iron-substituted MnSOD is catalytically inactive , although it was recently suggested that iron-substituted MnSOD has peroxidase/catalase activity . The binding constant for Mn(II) is 3...

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by rpoD (protein.P00579), soxS (protein.P0A9E2), marA (protein.P0ACH5), soxR (protein.P0ACS2).

## Enriched Pathways

- `eco04146` Peroxisome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00448|protein.P00448]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sodA; function=+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=sodA; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=sodA; function=+
- `activates` <-- [[protein.P0ACS2|protein.P0ACS2]] `RegulonDB` `S` - regulator=SoxR; target=sodA; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=sodA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012761,ECOCYC:EG10953,GeneID:948403`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4100810-4101430:+; feature_type=gene
