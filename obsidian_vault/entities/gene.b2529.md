---
entity_id: "gene.b2529"
entity_type: "gene"
name: "iscU"
source_database: "NCBI RefSeq"
source_id: "gene-b2529"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2529"
  - "iscU"
---

# iscU

`gene.b2529`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2529`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

iscU (gene.b2529) is a gene entity. It encodes iscU (protein.P0ACD4). Encoded protein function: FUNCTION: A scaffold on which IscS assembles Fe-S clusters. Exists as 2 interconverting forms, a structured (S) and disordered (D) form. The D-state is the preferred substrate for IscS. Converts to the S-state when an Fe-S cluster is assembled, which helps it dissociate from IscS to transfer the Fe-S to an acceptor. It is likely that Fe-S cluster coordination is flexible as the role of this complex is to build and then hand off Fe-S clusters. {ECO:0000269|PubMed:11577100, ECO:0000269|PubMed:22203963}. EcoCyc product frame: G7324-MONOMER. EcoCyc synonyms: yfhN, nifU. Genomic coordinates: 2659903-2660289. EcoCyc protein note: The assembly of iron-sulfur clusters requires complex biosynthetic machinery. E. coli encodes two sets of proteins, the Isc and the Suf system, to achieve this task. IscU is the scaffold protein for assembly and transfer of iron-sulfur clusters of the Isc system. The cysteine desulfurase CPLX0-248 IscS transfers the sulfane sulfur to IscU, EG12132-MONOMER IscA acts as the iron chaperone, EG11653-MONOMER CyaY appears to regulate cluster assembly, and the EG12130-MONOMER HscA and EG12131-MONOMER HscB chaperone and cochaperone facilitate Fe-S cluster transfer. An iron-first mechanism for Fe-S cluster assembly has been proposed...

## Biological Role

Repressed by ryhB (gene.b4451), iscR (protein.P0AGK8). Activated by oxyS (gene.b4458), rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACD4|protein.P0ACD4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[gene.b4458|gene.b4458]] `RegulonDB` `S` - regulator=OxyS; target=iscU; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=iscU; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=iscU; function=-
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `C` - regulator=IscR; target=iscU; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008321,ECOCYC:G7324,GeneID:947002`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2659903-2660289:-; feature_type=gene
