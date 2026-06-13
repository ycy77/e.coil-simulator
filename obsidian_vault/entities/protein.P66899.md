---
entity_id: "protein.P66899"
entity_type: "protein"
name: "ygeX"
source_database: "UniProt"
source_id: "P66899"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygeX b2871 JW2839"
---

# ygeX

`protein.P66899`

## Static

- Type: `protein`
- Source: `UniProt:P66899`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the alpha,beta-elimination reaction of both L- and D-alpha,beta-diaminopropionate (DAP) to form pyruvate and ammonia. In vitro the D-isomer of serine is degraded to pyruvate, though very poorly; other amino acids (L-serine, D- and L-threonine, D- and L-beta-Cl-alanine) are not substrates. In vivo allows poor growth on L-DAP or a DL-DAP mixture but not on D-DAP alone, this may be due to a poor promoter. DL-DAP is toxic in the absence of this enzyme, it may inhibit enzymes involved in the synthesis of pyruvate and aspartate, as well as amino acids derived from them. {ECO:0000269|PubMed:12596860, ECO:0000269|PubMed:12821154, ECO:0000269|PubMed:22505717, ECO:0000269|PubMed:22904288}. Unlike Salmonella typhimurium, E. coli only shows weak growth on 2,3-diaminopropionate as the sole source of carbon. This difference may be due to the very low expression levels of 2,3-diaminopropionate ammonia-lyase in E. coli . 2,3-Diaminopropionate ammonia-lyase is not stereospecific and catalyzes the α,β-elimination of both the D and L stereoisomer of 2,3-diaminopropionate . The enzyme also exhibits weak activity toward D-serine, and does not exhibit activity toward L-serine, D-β-Cl-alanine, or L-β-Cl-alanine . The enzyme is homodimeric and contains a pyridoxal 5'-phosphate prosthetic group , belonging to the fold-type II family of PLP-containing enzymes...

## Biological Role

Catalyzes 2,3-diaminopropanoate ammonia-lyase (adding water; pyruvate-forming) (reaction.R00195), serine ammonia-lyase (pyruvate-forming) (reaction.R00223). Component of 2,3-diaminopropionate ammonia-lyase (complex.ecocyc.CPLX0-1401).

## Annotation

FUNCTION: Catalyzes the alpha,beta-elimination reaction of both L- and D-alpha,beta-diaminopropionate (DAP) to form pyruvate and ammonia. In vitro the D-isomer of serine is degraded to pyruvate, though very poorly; other amino acids (L-serine, D- and L-threonine, D- and L-beta-Cl-alanine) are not substrates. In vivo allows poor growth on L-DAP or a DL-DAP mixture but not on D-DAP alone, this may be due to a poor promoter. DL-DAP is toxic in the absence of this enzyme, it may inhibit enzymes involved in the synthesis of pyruvate and aspartate, as well as amino acids derived from them. {ECO:0000269|PubMed:12596860, ECO:0000269|PubMed:12821154, ECO:0000269|PubMed:22505717, ECO:0000269|PubMed:22904288}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00195|reaction.R00195]] `KEGG` `database` - via EC:4.3.1.15
- `catalyzes` --> [[reaction.R00223|reaction.R00223]] `KEGG` `database` - via EC:4.3.1.15
- `is_component_of` --> [[complex.ecocyc.CPLX0-1401|complex.ecocyc.CPLX0-1401]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2871|gene.b2871]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P66899`
- `KEGG:ecj:JW2839;eco:b2871;ecoc:C3026_15750;`
- `GeneID:75205292;947012;`
- `GO:GO:0008838; GO:0030170; GO:0042803`
- `EC:4.3.1.15`

## Notes

Diaminopropionate ammonia-lyase (DAPAL) (EC 4.3.1.15) (2,3-diaminopropionate ammonia-lyase) (Alpha,beta-diaminopropionate ammonia-lyase) (Diaminopropionatase)
