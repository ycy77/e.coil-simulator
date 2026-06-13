---
entity_id: "protein.P0A6M4"
entity_type: "protein"
name: "dtd"
source_database: "UniProt"
source_id: "P0A6M4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00518, ECO:0000305|PubMed:4292198}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dtd yihZ b3887 JW3858"
---

# dtd

`protein.P0A6M4`

## Static

- Type: `protein`
- Source: `UniProt:P0A6M4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00518, ECO:0000305|PubMed:4292198}.

## Enriched Summary

FUNCTION: An aminoacyl-tRNA editing enzyme that deacylates mischarged D-aminoacyl-tRNAs, has no observable editing activity on tRNAs charged with cognate L-amino acid (PubMed:10383414, PubMed:10918062, PubMed:24302572, PubMed:27224426, PubMed:4292198). Edits mischarged glycyl-tRNA(Ala) more efficiently than AlaRS (PubMed:28362257). Acts via tRNA-based rather than protein-based catalysis (PubMed:24302572, PubMed:27224426, PubMed:28362257). Rejects correctly charged L-amino acid-tRNAs from its binding site rather than specifically recognizing incorrectly charged D-amino acid-tRNAs (PubMed:27224426). Hydrolyzes correctly charged, achiral, glycyl-tRNA(Gly); GTP-bound EF-Tu (tested with T.thermophilus EF-Tu AC Q5SHN6) protects charged glycyl-tRNA(Gly) from hydrolysis, while increasing Dtd levels or inactivating EF-Tu decreases protection (PubMed:27224426). Hydrolyzes mischarged glycyl-tRNA(Ala) (but not seryl-tRNA(Ala)) even in the presence of EF-Tu, edits about 4-fold better than the editing domain of AlaRS (PubMed:28362257). Has greater activity on glycyl-tRNA(Ala) than glycyl-tRNA(Gly) due in part to its recognition of the conserved tRNA(Ala) G3.U70 wobble base pair (PubMed:28362257). Binds D-amino acids but not L-amino acids (PubMed:16902403). Overexpression of E.coli or P.falciparum Dtd is toxic in E.coli, toxicity can be rescued by supplementation with Gly (PubMed:27224426)...

## Biological Role

Component of D-aminoacyl-tRNA deacylase (complex.ecocyc.CPLX0-3581).

## Annotation

FUNCTION: An aminoacyl-tRNA editing enzyme that deacylates mischarged D-aminoacyl-tRNAs, has no observable editing activity on tRNAs charged with cognate L-amino acid (PubMed:10383414, PubMed:10918062, PubMed:24302572, PubMed:27224426, PubMed:4292198). Edits mischarged glycyl-tRNA(Ala) more efficiently than AlaRS (PubMed:28362257). Acts via tRNA-based rather than protein-based catalysis (PubMed:24302572, PubMed:27224426, PubMed:28362257). Rejects correctly charged L-amino acid-tRNAs from its binding site rather than specifically recognizing incorrectly charged D-amino acid-tRNAs (PubMed:27224426). Hydrolyzes correctly charged, achiral, glycyl-tRNA(Gly); GTP-bound EF-Tu (tested with T.thermophilus EF-Tu AC Q5SHN6) protects charged glycyl-tRNA(Gly) from hydrolysis, while increasing Dtd levels or inactivating EF-Tu decreases protection (PubMed:27224426). Hydrolyzes mischarged glycyl-tRNA(Ala) (but not seryl-tRNA(Ala)) even in the presence of EF-Tu, edits about 4-fold better than the editing domain of AlaRS (PubMed:28362257). Has greater activity on glycyl-tRNA(Ala) than glycyl-tRNA(Gly) due in part to its recognition of the conserved tRNA(Ala) G3.U70 wobble base pair (PubMed:28362257). Binds D-amino acids but not L-amino acids (PubMed:16902403). Overexpression of E.coli or P.falciparum Dtd is toxic in E.coli, toxicity can be rescued by supplementation with Gly (PubMed:27224426). By recycling D-aminoacyl-tRNA to D-amino acids and free tRNA molecules, this enzyme counteracts the toxicity associated with the formation of D-aminoacyl-tRNA entities in vivo and helps enforce protein L-homochirality (PubMed:15292242). Hydrolyzes D-tyrosyl-tRNA(Tyr) (PubMed:10383414, PubMed:24302572, PubMed:27224426, PubMed:4292198). Hydrolyzes D-phenylalanyl-tRNA(Phe) (PubMed:24302572, PubMed:4292198). Hydrolyzes D-aspartyl-tRNA(Asp) (PubMed:10918062). Hydrolyzes D-tryptophanyl-tRNA(Trp) (PubMed:10918062). Hydrolyzes glycyl-tRNA(Gly) (PubMed:27224426). Hydrolyzes glycyl-tRNA(Ala) (PubMed:28362257). {ECO:0000269|PubMed:10383414, ECO:0000269|PubMed:10918062, ECO:0000269|PubMed:15292242, ECO:0000269|PubMed:16902403, ECO:0000269|PubMed:24302572, ECO:0000269|PubMed:25441601, ECO:0000269|PubMed:27224426, ECO:0000269|PubMed:28362257, ECO:0000269|PubMed:4292198}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3581|complex.ecocyc.CPLX0-3581]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3887|gene.b3887]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6M4`
- `KEGG:ecj:JW3858;eco:b3887;ecoc:C3026_21010;`
- `GeneID:86861989;93778051;948378;`
- `GO:GO:0000049; GO:0002161; GO:0005737; GO:0006399; GO:0009408; GO:0019478; GO:0042803; GO:0043908; GO:0051499; GO:0051500; GO:0106026; GO:0106074`
- `EC:3.1.1.96`

## Notes

D-aminoacyl-tRNA deacylase (DTD) (EC 3.1.1.96) (D-tyrosyl RNA deacylase) (D-tyrosyl-tRNA(Tyr) deacylase) (Gly-tRNA(Ala) deacylase) (Gly-tRNA(Gly) deacylase)
