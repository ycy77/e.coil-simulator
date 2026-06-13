---
entity_id: "protein.P0ADP7"
entity_type: "protein"
name: "ubiJ"
source_database: "UniProt"
source_id: "P0ADP7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02215, ECO:0000269|PubMed:30686758}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ubiJ yigP b3834 JW3811"
---

# ubiJ

`protein.P0ADP7`

## Static

- Type: `protein`
- Source: `UniProt:P0ADP7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02215, ECO:0000269|PubMed:30686758}.

## Enriched Summary

FUNCTION: Required for ubiquinone (coenzyme Q) biosynthesis under aerobic conditions (PubMed:24142253, PubMed:30686758). Binds hydrophobic ubiquinone biosynthetic intermediates via its SCP2 domain and is essential for the stability of the Ubi complex (PubMed:30686758). May constitute a docking platform where Ubi enzymes assemble and access their SCP2-bound polyprenyl substrates (PubMed:30686758). {ECO:0000269|PubMed:24142253, ECO:0000269|PubMed:30686758}. UbiJ is an accessory factor in ubiquinone biosynthesis that is part of the Ubi complex metabolon . The C terminus of UbiJ interacts directly with UbiK; the isolated proteins appear to form a 2:1 UbiK:UbiJ heterotrimer that is able to bind palmitoleate , ubiquinone-8, 2-octaprenylphenol, and C6-demethoxy-ubiquinone-8 . The N-terminal SCP2 domain of UbiJ is responsible for lipid binding . UbiJ predominantly localizes to the cytosol. The seven ubiquinone biosynthesis proteins UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK form a 1 MDa complex in the cytosol; UbiJ appears to be required for stability of the complex . The purified SCP2 domain of UbiJ homodimerizes; crystal structures of this domain have been solved . Although did not recover a yigP (ubiJ) null mutant strain, was able to construct such a mutant. Under aerobic growth conditions, this ubiJ mutant has a growth defect and does not contain any ubiquinone-8...

## Biological Role

Component of Ubi complex (complex.ecocyc.CPLX0-8301).

## Annotation

FUNCTION: Required for ubiquinone (coenzyme Q) biosynthesis under aerobic conditions (PubMed:24142253, PubMed:30686758). Binds hydrophobic ubiquinone biosynthetic intermediates via its SCP2 domain and is essential for the stability of the Ubi complex (PubMed:30686758). May constitute a docking platform where Ubi enzymes assemble and access their SCP2-bound polyprenyl substrates (PubMed:30686758). {ECO:0000269|PubMed:24142253, ECO:0000269|PubMed:30686758}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8301|complex.ecocyc.CPLX0-8301]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3834|gene.b3834]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADP7`
- `KEGG:ecj:JW3811;eco:b3834;ecoc:C3026_20745;`
- `GeneID:93778101;948915;`
- `GO:GO:0005737; GO:0006744; GO:0042802; GO:0110142`

## Notes

Ubiquinone biosynthesis accessory factor UbiJ
