---
entity_id: "gene.b1682"
entity_type: "gene"
name: "sufC"
source_database: "NCBI RefSeq"
source_id: "gene-b1682"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1682"
  - "sufC"
---

# sufC

`gene.b1682`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1682`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sufC (gene.b1682) is a gene entity. It encodes sufC (protein.P77499). Encoded protein function: FUNCTION: Has low ATPase activity. The SufBCD complex acts synergistically with SufE to stimulate the cysteine desulfurase activity of SufS. The SufBCD complex contributes to the assembly or repair of oxygen-labile iron-sulfur clusters under oxidative stress. May facilitate iron uptake from extracellular iron chelators under iron limitation. {ECO:0000269|PubMed:12554644, ECO:0000269|PubMed:12941942, ECO:0000269|PubMed:19810706}. EcoCyc product frame: G6908-MONOMER. EcoCyc synonyms: ynhD. Genomic coordinates: 1761766-1762512. EcoCyc protein note: The assembly of iron-sulfur clusters requires complex biosynthetic machinery. E. coli encodes two sets of proteins, the Isc and the Suf system, to achieve this task. SufC is a component of the SufBC2D Fe-S cluster assembly scaffold complex. SufC is a member of the ABC ATPase superfamily; its ATPase activity is required for iron acquisition in vivo, and both SufC and SufD are required for Fe-S cluster formation on SufB in vivo . A crystal structure of SufC has been determined at 2.5 Å resolution , and a crystal structure of the SufC2-SufD2 complex has been determined at 2.2 Å resolution . Upon associating with SufD, the structure of SufC changes to become competent for ATP binding and hydrolysis...

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by rpoD (protein.P00579), oxyR (protein.P0ACQ4), iscR (protein.P0AGK8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77499|protein.P77499]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sufC; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=sufC; function=+
- `activates` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=sufC; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=sufC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005619,ECOCYC:G6908,GeneID:946128`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1761766-1762512:-; feature_type=gene
