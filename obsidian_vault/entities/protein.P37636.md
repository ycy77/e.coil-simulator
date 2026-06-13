---
entity_id: "protein.P37636"
entity_type: "protein"
name: "mdtE"
source_database: "UniProt"
source_id: "P37636"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtE yhiU b3513 JW3481"
---

# mdtE

`protein.P37636`

## Static

- Type: `protein`
- Source: `UniProt:P37636`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}.

## Enriched Summary

FUNCTION: Part of the tripartite efflux system MdtEF-TolC, which confers resistance to compounds such as rhodamine 6G, erythromycin, doxorubicin, ethidium bromide, TPP, SDS, deoxycholate, crystal violet and benzalkonium. {ECO:0000269|PubMed:11566977}. MdtE is the membrane fusion protein of a putative tripartite efflux pump complex; production of the complex (through expression of cloned mdtEF genes) confers some degree of resistance to various toxic compounds in laboratory strains of E. coli K-12 (see TRANS-CPLX-204 for more detail). Production of MdtE does not complement the efflux defect of E. coli strain HNCE3 (nonpolar ΔacrA) (. MdtE is a member of the Membrane Fusion Protein (MFP) family . MdtE was isolated as a homotrimer in inner membrane vesicles purified from E. coli strain BL21 . Exposure to synthetic reactive oxygen species (ROS) generated from synthetron radiation (X-ray) results in oxidation of methionine residues in vivo in hundreds of proteins. The % modification was highest in MdtE, EG11009-MONOMER TolC and EG10855-MONOMER and increased as the X-ray oxidation dose increased .

## Biological Role

Component of multidrug efflux pump MdtEF-TolC (complex.ecocyc.TRANS-CPLX-204).

## Annotation

FUNCTION: Part of the tripartite efflux system MdtEF-TolC, which confers resistance to compounds such as rhodamine 6G, erythromycin, doxorubicin, ethidium bromide, TPP, SDS, deoxycholate, crystal violet and benzalkonium. {ECO:0000269|PubMed:11566977}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-204|complex.ecocyc.TRANS-CPLX-204]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3513|gene.b3513]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37636`
- `KEGG:ecj:JW3481;eco:b3513;ecoc:C3026_19035;`
- `GeneID:948031;`
- `GO:GO:0005886; GO:0009636; GO:0015125; GO:0015721; GO:0042802; GO:0042908; GO:0046677`

## Notes

Multidrug resistance protein MdtE
