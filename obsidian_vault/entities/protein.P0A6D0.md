---
entity_id: "protein.P0A6D0"
entity_type: "protein"
name: "argR"
source_database: "UniProt"
source_id: "P0A6D0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argR xerA b3237 JW3206"
---

# argR

`protein.P0A6D0`

## Static

- Type: `protein`
- Source: `UniProt:P0A6D0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Negatively controls the expression of the four operons of arginine biosynthesis in addition to the carAB operon. Predominantly interacts with A/T residues in ARG boxes. It also binds to a specific site in cer locus. Thus it is essential for cer-mediated site-specific recombination in ColE1. It is necessary for monomerization of the plasmid ColE1.

## Biological Role

Component of DNA-binding transcriptional dual regulator ArgR (complex.ecocyc.PC00005).

## Annotation

FUNCTION: Negatively controls the expression of the four operons of arginine biosynthesis in addition to the carAB operon. Predominantly interacts with A/T residues in ARG boxes. It also binds to a specific site in cer locus. Thus it is essential for cer-mediated site-specific recombination in ColE1. It is necessary for monomerization of the plasmid ColE1.

## Outgoing Edges (64)

- `activates` --> [[gene.b0045|gene.b0045]] `RegulonDB` `S` - regulator=ArgR; target=yaaU; function=+
- `activates` --> [[gene.b0112|gene.b0112]] `RegulonDB` `S` - regulator=ArgR; target=aroP; function=+
- `activates` --> [[gene.b1301|gene.b1301]] `RegulonDB` `S` - regulator=ArgR; target=puuB; function=+
- `activates` --> [[gene.b1744|gene.b1744]] `RegulonDB` `C` - regulator=ArgR; target=astE; function=+
- `activates` --> [[gene.b1745|gene.b1745]] `RegulonDB` `S` - regulator=ArgR; target=astB; function=+
- `activates` --> [[gene.b1746|gene.b1746]] `RegulonDB` `S` - regulator=ArgR; target=astD; function=+
- `activates` --> [[gene.b1747|gene.b1747]] `RegulonDB` `C` - regulator=ArgR; target=astA; function=+
- `activates` --> [[gene.b1748|gene.b1748]] `RegulonDB` `C` - regulator=ArgR; target=astC; function=+
- `activates` --> [[gene.b2462|gene.b2462]] `RegulonDB` `S` - regulator=ArgR; target=eutS; function=+
- `activates` --> [[gene.b2471|gene.b2471]] `RegulonDB` `S` - regulator=ArgR; target=yffB; function=+
- `activates` --> [[gene.b3151|gene.b3151]] `RegulonDB` `S` - regulator=ArgR; target=yraQ; function=+
- `activates` --> [[gene.b4077|gene.b4077]] `RegulonDB` `S` - regulator=ArgR; target=gltP; function=+
- `is_component_of` --> [[complex.ecocyc.PC00005|complex.ecocyc.PC00005]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `represses` --> [[gene.b0032|gene.b0032]] `RegulonDB` `C` - regulator=ArgR; target=carA; function=-
- `represses` --> [[gene.b0033|gene.b0033]] `RegulonDB` `C` - regulator=ArgR; target=carB; function=-
- `represses` --> [[gene.b0095|gene.b0095]] `RegulonDB` `S` - regulator=ArgR; target=ftsZ; function=-
- `represses` --> [[gene.b0273|gene.b0273]] `RegulonDB` `C` - regulator=ArgR; target=argF; function=-
- `represses` --> [[gene.b0812|gene.b0812]] `RegulonDB` `S` - regulator=ArgR; target=dps; function=-
- `represses` --> [[gene.b0839|gene.b0839]] `RegulonDB` `S` - regulator=ArgR; target=dacC; function=-
- `represses` --> [[gene.b0854|gene.b0854]] `RegulonDB` `S` - regulator=ArgR; target=potF; function=-
- `represses` --> [[gene.b0860|gene.b0860]] `RegulonDB` `C` - regulator=ArgR; target=artJ; function=-
- `represses` --> [[gene.b0861|gene.b0861]] `RegulonDB` `C` - regulator=ArgR; target=artM; function=-
- `represses` --> [[gene.b0862|gene.b0862]] `RegulonDB` `C` - regulator=ArgR; target=artQ; function=-
- `represses` --> [[gene.b0863|gene.b0863]] `RegulonDB` `C` - regulator=ArgR; target=artI; function=-
- `represses` --> [[gene.b0864|gene.b0864]] `RegulonDB` `C` - regulator=ArgR; target=artP; function=-
- `represses` --> [[gene.b0874|gene.b0874]] `RegulonDB` `C` - regulator=ArgR; target=lysO; function=-
- `represses` --> [[gene.b0889|gene.b0889]] `RegulonDB` `S` - regulator=ArgR; target=lrp; function=-
- `represses` --> [[gene.b0923|gene.b0923]] `RegulonDB` `S` - regulator=ArgR; target=mukE; function=-
- `represses` --> [[gene.b1605|gene.b1605]] `RegulonDB` `S` - regulator=ArgR; target=ydgI; function=-
- `represses` --> [[gene.b1723|gene.b1723]] `RegulonDB` `S` - regulator=ArgR; target=pfkB; function=-
- `represses` --> [[gene.b1967|gene.b1967]] `RegulonDB` `S` - regulator=ArgR; target=hchA; function=-
- `represses` --> [[gene.b2018|gene.b2018]] `RegulonDB` `S` - regulator=ArgR; target=hisL; function=-
- `represses` --> [[gene.b2298|gene.b2298]] `RegulonDB` `S` - regulator=ArgR; target=yfcC; function=-
- `represses` --> [[gene.b2306|gene.b2306]] `RegulonDB` `C` - regulator=ArgR; target=hisP; function=-
- `represses` --> [[gene.b2307|gene.b2307]] `RegulonDB` `C` - regulator=ArgR; target=hisM; function=-
- `represses` --> [[gene.b2308|gene.b2308]] `RegulonDB` `C` - regulator=ArgR; target=hisQ; function=-
- `represses` --> [[gene.b2309|gene.b2309]] `RegulonDB` `C` - regulator=ArgR; target=hisJ; function=-
- `represses` --> [[gene.b2313|gene.b2313]] `RegulonDB` `S` - regulator=ArgR; target=cvpA; function=-
- `represses` --> [[gene.b2669|gene.b2669]] `RegulonDB` `S` - regulator=ArgR; target=stpA; function=-
- `represses` --> [[gene.b2818|gene.b2818]] `RegulonDB` `C` - regulator=ArgR; target=argA; function=-
- `represses` --> [[gene.b3164|gene.b3164]] `RegulonDB` `S` - regulator=ArgR; target=pnp; function=-
- `represses` --> [[gene.b3165|gene.b3165]] `RegulonDB` `S` - regulator=ArgR; target=rpsO; function=-
- `represses` --> [[gene.b3166|gene.b3166]] `RegulonDB` `S` - regulator=ArgR; target=truB; function=-
- `represses` --> [[gene.b3167|gene.b3167]] `RegulonDB` `S` - regulator=ArgR; target=rbfA; function=-
- `represses` --> [[gene.b3168|gene.b3168]] `RegulonDB` `S` - regulator=ArgR; target=infB; function=-
- `represses` --> [[gene.b3169|gene.b3169]] `RegulonDB` `S` - regulator=ArgR; target=nusA; function=-
- `represses` --> [[gene.b3170|gene.b3170]] `RegulonDB` `S` - regulator=ArgR; target=rimP; function=-
- `represses` --> [[gene.b3171|gene.b3171]] `RegulonDB` `S` - regulator=ArgR; target=metY; function=-
- `represses` --> [[gene.b3172|gene.b3172]] `RegulonDB` `S` - regulator=ArgR; target=argG; function=-
- `represses` --> [[gene.b3211|gene.b3211]] `RegulonDB` `C` - regulator=ArgR; target=yhcC; function=-
- `represses` --> [[gene.b3212|gene.b3212]] `RegulonDB` `S` - regulator=ArgR; target=gltB; function=-
- `represses` --> [[gene.b3213|gene.b3213]] `RegulonDB` `S` - regulator=ArgR; target=gltD; function=-
- `represses` --> [[gene.b3214|gene.b3214]] `RegulonDB` `S` - regulator=ArgR; target=gltF; function=-
- `represses` --> [[gene.b3237|gene.b3237]] `RegulonDB` `C` - regulator=ArgR; target=argR; function=-
- `represses` --> [[gene.b3359|gene.b3359]] `RegulonDB` `S` - regulator=ArgR; target=argD; function=-
- `represses` --> [[gene.b3390|gene.b3390]] `RegulonDB` `S` - regulator=ArgR; target=aroK; function=-
- `represses` --> [[gene.b3633|gene.b3633]] `RegulonDB` `S` - regulator=ArgR; target=waaA; function=-
- `represses` --> [[gene.b3957|gene.b3957]] `RegulonDB` `C` - regulator=ArgR; target=argE; function=-
- `represses` --> [[gene.b3958|gene.b3958]] `RegulonDB` `C` - regulator=ArgR; target=argC; function=-
- `represses` --> [[gene.b3959|gene.b3959]] `RegulonDB` `C` - regulator=ArgR; target=argB; function=-
- `represses` --> [[gene.b3960|gene.b3960]] `RegulonDB` `C` - regulator=ArgR; target=argH; function=-
- `represses` --> [[gene.b4246|gene.b4246]] `RegulonDB` `S` - regulator=ArgR; target=pyrL; function=-
- `represses` --> [[gene.b4254|gene.b4254]] `RegulonDB` `C` - regulator=ArgR; target=argI; function=-
- `represses` --> [[gene.b4426|gene.b4426]] `RegulonDB` `S` - regulator=ArgR; target=mcaS; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3237|gene.b3237]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6D0`
- `KEGG:ecj:JW3206;eco:b3237;ecoc:C3026_17610;`
- `GeneID:93778748;947861;`
- `GO:GO:0000821; GO:0000987; GO:0003700; GO:0005667; GO:0005737; GO:0006526; GO:0034618; GO:0042150; GO:0042802; GO:0051259; GO:1900079; GO:1900081; GO:2000143; GO:2000144`

## Notes

Arginine repressor
